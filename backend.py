from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import io

app = FastAPI()

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    # Read file as bytes
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

    width, height = image.size

    return JSONResponse({
        "filename": file.filename,
        "width": width,
        "height": height,
        "message": "Image received successfully!"
    })
