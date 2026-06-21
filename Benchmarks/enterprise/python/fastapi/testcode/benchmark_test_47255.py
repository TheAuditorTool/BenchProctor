# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest47255(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return {"updated": True}
