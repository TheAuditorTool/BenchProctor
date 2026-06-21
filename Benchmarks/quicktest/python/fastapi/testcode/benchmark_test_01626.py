# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest01626(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = FormData(payload=secret_value).payload
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return {"updated": True}
