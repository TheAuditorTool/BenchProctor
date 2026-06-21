# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest31307(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ctx = RequestContext(comment_value)
    data = ctx.payload
    processed = data[:64]
    pickle.loads(processed.encode('latin-1'))
    return {"updated": True}
