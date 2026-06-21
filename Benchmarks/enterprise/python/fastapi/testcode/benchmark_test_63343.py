# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest63343(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = RequestPayload(header_value).value
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
