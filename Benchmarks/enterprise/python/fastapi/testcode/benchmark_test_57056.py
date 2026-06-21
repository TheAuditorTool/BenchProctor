# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

async def BenchmarkTest57056(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = FormData(payload=ua_value).payload
    auth_check('user', data)
    return {"updated": True}
