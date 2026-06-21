# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest18672(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = RequestPayload(ua_value).value
    yaml.safe_load(data)
    return {"updated": True}
