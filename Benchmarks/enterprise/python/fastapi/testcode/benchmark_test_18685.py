# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest18685(request: Request, field: str = Form('')):
    field_value = field
    data = RequestPayload(field_value).value
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
