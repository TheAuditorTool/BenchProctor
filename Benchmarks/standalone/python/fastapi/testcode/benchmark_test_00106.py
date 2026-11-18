# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import subprocess
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


@app.post("/BenchmarkTest00106")
async def BenchmarkTest00106(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    reader = make_reader(header_value)
    data = reader()
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
