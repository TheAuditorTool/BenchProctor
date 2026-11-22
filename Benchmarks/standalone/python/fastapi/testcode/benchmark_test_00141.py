# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import io
import defusedxml.ElementTree
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


@app.post("/BenchmarkTest00141")
async def BenchmarkTest00141(request: Request, req: UserInput):
    json_value = req.payload
    data = (lambda v: v.strip())(json_value)
    for _event, element in defusedxml.ElementTree.iterparse(io.BytesIO(str(data).encode()), events=('end',)):
        element.clear()
    return {"updated": True}
