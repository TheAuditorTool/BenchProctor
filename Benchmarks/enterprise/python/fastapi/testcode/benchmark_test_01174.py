# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest01174(request: Request):
    user_id = request.query_params.get('id', '')
    data = RequestPayload(user_id).value
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
