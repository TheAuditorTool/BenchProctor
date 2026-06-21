# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest53034(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = FormData(payload=forwarded_ip).payload
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
