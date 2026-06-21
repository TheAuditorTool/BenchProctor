# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest25554(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    ctx = RequestContext(dotenv_value)
    data = ctx.payload
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
