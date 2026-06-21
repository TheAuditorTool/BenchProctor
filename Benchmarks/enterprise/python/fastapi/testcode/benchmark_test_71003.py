# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest71003(request: Request):
    path_value = request.path_params.get('id', '')
    data = RequestPayload(path_value).value
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return {"updated": True}
