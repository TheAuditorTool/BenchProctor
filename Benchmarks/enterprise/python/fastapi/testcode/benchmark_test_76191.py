# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest76191(request: Request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = FormData(payload=secret_value).payload
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return {"updated": True}
