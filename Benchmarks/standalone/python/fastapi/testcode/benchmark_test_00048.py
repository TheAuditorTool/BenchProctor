# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from fastapi import HTTPException
from urllib.parse import urlparse
from dataclasses import dataclass
from starlette.responses import JSONResponse
import re


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


@app.post("/BenchmarkTest00048/{id}")
async def BenchmarkTest00048(request: Request, id: str):
    path_value = id
    form = FormData(payload=path_value)
    data = form.payload
    parsed = urlparse(data)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", data) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    raise HTTPException(status_code=303, headers={'Location': str(target_url)})
