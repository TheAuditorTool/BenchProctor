# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest43929(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
