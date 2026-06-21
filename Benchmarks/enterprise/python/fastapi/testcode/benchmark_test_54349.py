# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest54349(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = RequestPayload(header_value).value
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
