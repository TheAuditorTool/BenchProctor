# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db, User


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest22151(request: Request):
    path_value = request.path_params.get('id', '')
    ctx = RequestContext(path_value)
    data = ctx.payload
    db.session.query(User).filter(User.id == data).all()
    return {"updated": True}
