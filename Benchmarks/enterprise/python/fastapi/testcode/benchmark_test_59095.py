# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest59095(request: Request):
    origin_value = request.headers.get('origin', '')
    data = RequestPayload(origin_value).value
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
