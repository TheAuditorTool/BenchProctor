# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest05892(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
