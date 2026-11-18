# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from cryptography.fernet import Fernet
from starlette.responses import JSONResponse
import os


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00129")
async def BenchmarkTest00129(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    parts = str(xml_value).split(',')
    data = ' '.join(parts)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
