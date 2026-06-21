# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
from app_runtime import db


async def BenchmarkTest47438(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data, _sep, _rest = str(comment_value).partition('\x00')
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
