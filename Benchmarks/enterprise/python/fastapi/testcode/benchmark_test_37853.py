# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest37853(request: Request):
    user_id = request.query_params.get('id', '')
    data = RequestPayload(user_id).value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
