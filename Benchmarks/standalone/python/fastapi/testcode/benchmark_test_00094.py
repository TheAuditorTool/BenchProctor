# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import requests
from app_runtime import db
from fastapi.responses import JSONResponse


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00094")
async def BenchmarkTest00094(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = str(comment_value).replace('\x00', '')
    requests.get(str(data))
    return {"updated": True}
