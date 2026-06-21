# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest54552(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    ctx = RequestContext(config_value)
    data = ctx.payload
    logging.info('User action: ' + str(data))
    return {"updated": True}
