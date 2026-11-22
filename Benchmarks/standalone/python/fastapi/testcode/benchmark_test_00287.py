# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from Crypto.Hash import MD4
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''
def make_reader(raw):
    def read():
        return raw.strip()
    return read

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00287")
async def BenchmarkTest00287(request: Request, req: UserInput):
    json_value = req.payload
    reader = make_reader(json_value)
    data = reader()
    digest = MD4.new(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
