# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from fastapi import Form
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


@app.post("/BenchmarkTest00035")
async def BenchmarkTest00035(request: Request, field: str = Form('')):
    field_value = field
    reader = make_reader(field_value)
    data = reader()
    eval(str(data))
    return {"updated": True}
