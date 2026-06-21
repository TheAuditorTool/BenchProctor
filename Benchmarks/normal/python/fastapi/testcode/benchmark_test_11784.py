# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest11784(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = FormData(payload=secret_value).payload
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return {"updated": True}
