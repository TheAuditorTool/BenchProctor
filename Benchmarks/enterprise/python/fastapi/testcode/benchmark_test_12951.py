# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest12951(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
