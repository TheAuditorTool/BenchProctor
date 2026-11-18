# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import os
from fastapi.responses import JSONResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00599")
async def BenchmarkTest00599(request: Request):
    origin_value = request.headers.get('origin', '')
    reader = make_reader(origin_value)
    data = reader()
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    os.unlink(checked_path)
    return {"updated": True}
