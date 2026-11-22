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


@app.post("/BenchmarkTest00250")
async def BenchmarkTest00250(request: Request):
    user_id = request.query_params.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
