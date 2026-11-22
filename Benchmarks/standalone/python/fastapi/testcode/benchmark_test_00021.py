# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from fastapi import HTTPException
from dataclasses import dataclass
from fastapi.responses import JSONResponse


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


@app.post("/BenchmarkTest00021")
async def BenchmarkTest00021(request: Request):
    upload_name = getattr((await request.form()).get('upload'), 'filename', '')
    form = FormData(payload=upload_name)
    data = form.payload
    raise HTTPException(status_code=303, headers={'Location': str(data)})
