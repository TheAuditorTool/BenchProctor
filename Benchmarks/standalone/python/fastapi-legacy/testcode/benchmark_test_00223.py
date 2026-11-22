# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import io
import xml.sax
import defusedxml.sax
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


@app.post("/BenchmarkTest00223")
async def BenchmarkTest00223(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    parser = defusedxml.sax.make_parser()
    parser.setContentHandler(xml.sax.ContentHandler())
    parser.parse(io.StringIO(str(data)))
    return {"updated": True}
