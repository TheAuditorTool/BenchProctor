# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
import os
from starlette.responses import JSONResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest53745(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
