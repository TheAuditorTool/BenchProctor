# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest20052(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
