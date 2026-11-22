# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import io
import xml.sax
import defusedxml.sax
from fastapi import Form
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


@app.post("/BenchmarkTest00147")
async def BenchmarkTest00147(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % str(field_value)
    parser = defusedxml.sax.make_parser()
    parser.setContentHandler(xml.sax.ContentHandler())
    parser.parse(io.StringIO(str(data)))
    return {"updated": True}
