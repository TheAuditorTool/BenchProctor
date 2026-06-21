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

async def BenchmarkTest58671(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = RequestPayload(multipart_value).value
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
