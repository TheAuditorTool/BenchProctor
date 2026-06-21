# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest27770(request: Request):
    user_id = request.query_params.get('id', '')
    data = RequestPayload(user_id).value
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
