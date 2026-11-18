# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from fastapi import Form
import base64
import pickle
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


@app.post("/BenchmarkTest00654")
async def BenchmarkTest00654(request: Request, field: str = Form('')):
    field_value = field
    data = '{}'.format(field_value)
    pickle.loads(base64.b64decode(data))
    return {"updated": True}
