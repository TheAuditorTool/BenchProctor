# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import Response
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


@app.post("/BenchmarkTest00081")
async def BenchmarkTest00081(request: Request):
    referer_value = request.headers.get('referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    return Response(status_code=302, headers={'Location': str(data)})
