# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest31941(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    ctx = RequestContext(prop_value)
    data = ctx.payload
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
