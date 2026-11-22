# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import io
import xml.sax
import defusedxml.sax
from pydantic import BaseModel
from fastapi.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00349")
async def BenchmarkTest00349(request: Request, req: UserInput):
    json_value = req.payload
    def normalize(value):
        return value.strip()
    data = normalize(json_value)
    parser = defusedxml.sax.make_parser()
    parser.setContentHandler(xml.sax.ContentHandler())
    parser.parse(io.StringIO(str(data)))
    return {"updated": True}
