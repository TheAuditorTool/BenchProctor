# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest67257(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request.session['data'] = str(comment_value)
    return {"updated": True}
