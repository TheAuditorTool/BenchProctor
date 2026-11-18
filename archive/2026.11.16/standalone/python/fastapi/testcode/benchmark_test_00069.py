# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from cryptography.fernet import Fernet
from dataclasses import dataclass
from starlette.responses import JSONResponse
import os


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00069")
async def BenchmarkTest00069(request: Request):
    user_id = request.query_params.get('id', '')
    form = FormData(payload=user_id)
    data = form.payload
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
