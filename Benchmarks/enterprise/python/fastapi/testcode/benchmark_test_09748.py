# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest09748(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
