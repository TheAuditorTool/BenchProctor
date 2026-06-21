# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from app_runtime import db


async def BenchmarkTest33405(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '{}'.format(comment_value)
    globals()['counter'] = int(data)
    return {"updated": True}
