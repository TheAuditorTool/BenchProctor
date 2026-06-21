# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest21991(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = RequestPayload(prop_value).value
    logging.info('User action: ' + str(data))
    return {"updated": True}
