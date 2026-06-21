# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest35605(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ctx = RequestContext(comment_value)
    data = ctx.payload
    logging.info('User action: ' + str(data))
    return {"updated": True}
