# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest12511(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = RequestPayload(secret_value).value
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return {"updated": True}
