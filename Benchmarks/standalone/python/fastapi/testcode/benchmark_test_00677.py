# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from pydantic import BaseModel
from app_runtime import db
from fastapi.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00677")
async def BenchmarkTest00677(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    db.execute("SELECT * FROM users WHERE id = '" + str(data) + "'")
    return {"updated": True}
