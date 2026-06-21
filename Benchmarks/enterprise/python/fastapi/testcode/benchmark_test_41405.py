# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import importlib


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest41405(request: Request, field: str = Form('')):
    field_value = field
    data = RequestPayload(field_value).value
    importlib.import_module(str(data))
    return {"updated": True}
