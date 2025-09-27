

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import crop_recommendation_router


origins = ["*"]


app = FastAPI()
app.include_router(crop_recommendation_router.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


