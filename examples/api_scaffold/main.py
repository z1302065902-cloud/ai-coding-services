"""最小 FastAPI 骨架 —— 演示交付形态。"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Sample API", version="0.1.0")


class EchoIn(BaseModel):
    message: str


class EchoOut(BaseModel):
    message: str
    length: int


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/echo", response_model=EchoOut)
def echo(body: EchoIn) -> EchoOut:
    return EchoOut(message=body.message, length=len(body.message))
