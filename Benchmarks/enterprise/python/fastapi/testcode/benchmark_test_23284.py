# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest23284(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return JSONResponse({'status': 'ok'}, status_code=200, headers={'Access-Control-Allow-Origin': origin})
    return {"updated": True}
