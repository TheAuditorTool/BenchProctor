# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import Response
import requests
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


@app.post("/BenchmarkTest00336")
async def BenchmarkTest00336(request: Request):
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    kind = 'json' if str(api_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(api_value).strip()
        case _:
            data = str(api_value)
    return Response(status_code=302, headers={'Location': str(data)})
