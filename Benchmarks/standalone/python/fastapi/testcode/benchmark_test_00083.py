# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from lxml import etree
from starlette.responses import JSONResponse
import re


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00083/{id}")
async def BenchmarkTest00083(request: Request, id: str):
    path_value = id
    if not re.fullmatch("^(asc|desc|name|created)$", str(path_value)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = path_value
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return {"updated": True}
