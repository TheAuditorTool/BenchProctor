# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import pickle


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest81100(request: Request, field: str = Form('')):
    field_value = field
    data = RequestPayload(field_value).value
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
