# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


async def BenchmarkTest11254(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    pending = list(str(comment_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    os.remove(str(data))
    return {"updated": True}
