# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from app_runtime import db


async def BenchmarkTest11359(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data, _sep, _rest = str(comment_value).partition('\x00')
    globals()['counter'] = int(data)
    return {"updated": True}
