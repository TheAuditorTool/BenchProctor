# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest31578(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = RequestPayload(db_value).value
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
