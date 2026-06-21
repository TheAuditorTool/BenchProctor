# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest12405(request: Request):
    user_id = request.query_params.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    db.execute('SELECT * FROM users WHERE id = :id', {'id': data})
    return {"updated": True}
