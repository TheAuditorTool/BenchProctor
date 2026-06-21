# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest26682(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = FormData(payload=raw_body).payload
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
