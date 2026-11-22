# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from fastapi import HTTPException
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


@app.post("/BenchmarkTest00322")
async def BenchmarkTest00322(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % str(origin_value)
    raise HTTPException(status_code=303, headers={'Location': str(data)})
