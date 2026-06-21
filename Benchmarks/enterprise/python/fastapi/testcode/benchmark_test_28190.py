# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

async def BenchmarkTest28190(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    auth_check('user', data)
    return {"updated": True}
