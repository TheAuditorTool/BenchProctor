# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest19451(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
