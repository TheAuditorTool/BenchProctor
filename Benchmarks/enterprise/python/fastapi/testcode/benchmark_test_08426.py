# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


async def BenchmarkTest08426(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    os.remove(str(comment_value))
    return {"updated": True}
