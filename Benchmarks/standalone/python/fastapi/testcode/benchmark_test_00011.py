# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from pathlib import Path
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


@app.post("/BenchmarkTest00011")
async def BenchmarkTest00011(request: Request):
    referer_value = request.headers.get('referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    Path('/var/app/data/' + str(data)).write_text('data')
    return {"updated": True}
