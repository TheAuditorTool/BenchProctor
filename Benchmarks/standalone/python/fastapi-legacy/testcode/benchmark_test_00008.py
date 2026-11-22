# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
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


@app.post("/BenchmarkTest00008")
async def BenchmarkTest00008(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % str(referer_value)
    pickle.loads(base64.b64decode(data))
    return {"updated": True}
