import cv2
import numpy as np
import uuid
import os
import requests
from fastapi import FastAPI, UploadFile, File, Query, HTTPException
from typing import Optional

app = FastAPI(title="Person Detection API")

PROTOTXT = "deploy.prototxt"
MODEL = "mobilenet_iter_73000.caffemodel"
CONFIDENCE_THRESHOLD = 0.5

tasks = {}

net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)


def detect_persons(image_np, task_id: str):
    (h, w) = image_np.shape[:2]
    blob = cv2.dnn.blobFromImage(
        cv2.resize(image_np, (300, 300)),
        0.007843,
        (300, 300),
        127.5
    )

    net.setInput(blob)
    detections = net.forward()

    count = 0
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > CONFIDENCE_THRESHOLD:
            idx = int(detections[0, 0, i, 1])

            if idx == 15:
                count += 1
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                cv2.rectangle(
                    image_np,
                    (startX, startY),
                    (endX, endY),
                    (0, 255, 0),
                    2
                )

    output_path = f"output_{task_id}.jpg"
    cv2.imwrite(output_path, image_np)

    return count


@app.get("/detect/local")
async def detect_local(filename: str):
    if not os.path.exists(filename):
        raise HTTPException(
            status_code=404,
            detail="Plik nie istnieje na serwerze"
        )

    task_id = str(uuid.uuid4())
    image = cv2.imread(filename)
    count = detect_persons(image, task_id)

    result = {"task_id": task_id, "person_count": count, "status": "completed"}
    tasks[task_id] = result
    return result


@app.get("/detect/url")
async def detect_url(url: str = Query(...)):
    task_id = str(uuid.uuid4())
    try:
        resp = requests.get(url)
        image_array = np.asarray(bytearray(resp.content), dtype="uint8")
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

        count = detect_persons(image, task_id)
        result = {
            "task_id": task_id,
            "person_count": count,
            "status": "completed"
        }
        tasks[task_id] = result
        return result
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Błąd pobierania zdjęcia: {str(e)}"
        )


@app.post("/detect/upload")
async def detect_upload(file: UploadFile = File(...)):
    task_id = str(uuid.uuid4())
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    count = detect_persons(image, task_id)
    result = {"task_id": task_id, "person_count": count, "status": "completed"}
    tasks[task_id] = result
    return result


@app.get("/status/{task_id}")
async def get_status(task_id: str):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Nie znaleziono zadania o tym ID"
        )
    return tasks[task_id]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
