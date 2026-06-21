# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def to_text(value):
    return str(value).strip()

async def BenchmarkTest66788(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = to_text(comment_value)
    request.session['data'] = str(data)
    return {"updated": True}
