# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest45441(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    trusted_claim = str(data)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
