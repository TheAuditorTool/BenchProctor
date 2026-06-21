# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest01515(request: Request):
    path_value = request.path_params.get('id', '')
    data = RequestPayload(path_value).value
    auth_check('user', data)
    return {"updated": True}
