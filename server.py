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
    twitter_acount: str
    content: str

@app.post("/process_text")
async def process_text(data: TextData):
    twitter_acount = data.twitter_acount
    content = data.content
    message = f"Account: {twitter_acount}\nContent: {content}\nSuccessful processing!\nWell done Samson!"
    
    return {"message": message}

@app.post("/generate_image")
async def generate_image(data: TextData):
    # Path to the image
    image_path = os.path.join(os.path.dirname(__file__), "cat.png")
    
    # Check if the file exists
    if not os.path.exists(image_path):
        return {"error": "Image file not found"}

    # Return the image as a response
    return FileResponse(image_path, media_type="image/png")
