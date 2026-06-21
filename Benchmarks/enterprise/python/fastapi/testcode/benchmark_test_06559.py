# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db, auth_check


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest06559(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ctx = RequestContext(comment_value)
    data = ctx.payload
    auth_check('user', data)
    return {"updated": True}
