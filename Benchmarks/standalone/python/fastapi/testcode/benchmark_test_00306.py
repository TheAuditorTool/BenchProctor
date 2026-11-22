# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import numpy as np
from pydantic import BaseModel
from starlette.responses import JSONResponse


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


@app.post("/BenchmarkTest00306")
async def BenchmarkTest00306(request: Request, req: UserInput):
    json_value = req.payload
    data = '%s' % (json_value,)
    quantity = int(str(data))
    total_cents = np.int32(quantity) * np.int32(1999)
    return JSONResponse({'total_cents': int(total_cents)}, status_code=200)
