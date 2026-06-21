# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest16244(request: Request):
    origin_value = request.headers.get('origin', '')
    data = RequestPayload(origin_value).value
    logging.info('User action: ' + str(data))
    return {"updated": True}
