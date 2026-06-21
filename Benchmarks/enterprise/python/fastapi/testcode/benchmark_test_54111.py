# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest54111(request: Request):
    query_array = request.query_params.get('items', '')
    data = RequestPayload(query_array).value
    logging.info('User action: ' + str(data))
    return {"updated": True}
