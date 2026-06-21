# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest51257(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ctx = RequestContext(comment_value)
    data = ctx.payload
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return {"updated": True}
