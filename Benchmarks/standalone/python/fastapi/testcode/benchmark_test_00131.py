# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import yaml
import json
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


@app.post("/BenchmarkTest00131")
async def BenchmarkTest00131(request: Request):
    upload_name = getattr((await request.form()).get('upload'), 'filename', '')
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
