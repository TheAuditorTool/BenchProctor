# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest67765(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = coalesce_blank(comment_value)
    os.remove(str(data))
    return {"updated": True}
