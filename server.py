import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextData(BaseModel):
    text: str

# Middleware to log requests
@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Log the request method and URL
    print(f"Received request: {request.method} {request.url}")
    response = await call_next(request)
    # Log the response status code
    print(f"Response status: {response.status_code}")
    return response

@app.post("/process_text")
async def process_text(data: TextData):
    # Optionally process the text here
    return {"message": "You have successfully sent texts!"}

@app.post("/generate_image")
async def generate_image(data: TextData):
    # Path to the image
    image_path = os.path.join(os.path.dirname(__file__), "cat.png")
    
    # Check if the file exists
    if not os.path.exists(image_path):
        return {"error": "Image file not found"}

    # Return the image as a response
    return FileResponse(image_path, media_type="image/png")
