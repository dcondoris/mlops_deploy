from fastapi import FastAPI

api = FastAPI(title="MLOps")


@api.get("/")
def status():
    return "Good evening everyone!"
