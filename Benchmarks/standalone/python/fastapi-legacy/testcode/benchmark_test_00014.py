# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import io
from lxml import etree
import base64
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


@app.post("/BenchmarkTest00014")
async def BenchmarkTest00014(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    for _event, element in etree.iterparse(io.BytesIO(str(data).encode()), events=('end',), load_dtd=True, resolve_entities=True, no_network=False):
        element.clear()
    return {"updated": True}
