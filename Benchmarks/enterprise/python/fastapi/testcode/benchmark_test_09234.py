# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest09234(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = FormData(payload=ua_value).payload
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(data)})
