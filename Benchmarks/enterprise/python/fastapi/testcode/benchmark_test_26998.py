# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from starlette.responses import JSONResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest26998(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = RequestPayload(config_value).value
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
