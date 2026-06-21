# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest18519(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(data)})
