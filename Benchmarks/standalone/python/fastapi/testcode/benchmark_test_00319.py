# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import hashlib
import json
from starlette.responses import JSONResponse


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00319")
async def BenchmarkTest00319(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    digest = hashlib.sha3_256(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
