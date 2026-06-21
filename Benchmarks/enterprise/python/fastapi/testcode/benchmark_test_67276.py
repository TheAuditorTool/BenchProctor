# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest67276(request: Request):
    user_id = request.query_params.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return {"updated": True}
