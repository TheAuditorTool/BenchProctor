# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import subprocess
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


@app.post("/BenchmarkTest00184")
async def BenchmarkTest00184(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '{}'.format(referer_value)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
