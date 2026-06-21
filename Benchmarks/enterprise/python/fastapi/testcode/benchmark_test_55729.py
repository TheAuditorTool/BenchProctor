# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest55729(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    ctx = RequestContext(dotenv_value)
    data = ctx.payload
    logging.info('User action: ' + str(data))
    return {"updated": True}
