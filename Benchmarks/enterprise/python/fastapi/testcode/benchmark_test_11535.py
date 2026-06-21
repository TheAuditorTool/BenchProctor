# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest11535(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    logging.info('User action: ' + str(data))
    return {"updated": True}
