# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest26945(request: Request):
    ua_value = request.headers.get('user-agent', '')
    ctx = RequestContext(ua_value)
    data = ctx.payload
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
