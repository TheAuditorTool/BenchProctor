# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest46270(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = FormData(payload=forwarded_ip).payload
    if str(data).startswith(('10.', '192.168.', '127.')):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
