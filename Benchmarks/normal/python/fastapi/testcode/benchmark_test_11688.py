# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest11688(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = RequestPayload(cookie_value).value
    logging.info('User action: ' + str(data))
    return {"updated": True}
