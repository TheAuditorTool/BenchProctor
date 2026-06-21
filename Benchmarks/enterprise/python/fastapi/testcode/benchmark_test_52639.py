# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest52639(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    requests.get(str(data))
    return {"updated": True}
