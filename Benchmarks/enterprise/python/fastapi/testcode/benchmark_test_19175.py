# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest19175(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = RequestPayload(auth_header).value
    logging.info('User action: ' + str(data))
    return {"updated": True}
