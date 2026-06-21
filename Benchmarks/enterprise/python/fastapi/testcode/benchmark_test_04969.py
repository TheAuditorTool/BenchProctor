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

async def BenchmarkTest04969(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = RequestPayload(upload_name).value
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
