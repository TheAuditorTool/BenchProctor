# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import auth_check


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest22320(request: Request, field: str = Form('')):
    field_value = field
    data = RequestPayload(field_value).value
    auth_check('user', data)
    return {"updated": True}
