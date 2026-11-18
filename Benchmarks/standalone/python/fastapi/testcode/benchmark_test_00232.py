# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import defusedxml.ElementTree
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


@app.post("/BenchmarkTest00232")
async def BenchmarkTest00232(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = '{}'.format(multipart_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
