# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest41273(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = RequestPayload(xml_value).value
    logging.info('User action: ' + str(data))
    return {"updated": True}
