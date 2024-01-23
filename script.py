from fastapi import FastAPI

api = FastAPI(title="MLOps")


@api.get("/")
def status():
    return "Bonjour tout le monde !"
