# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
from app_runtime import db


async def BenchmarkTest04702(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(comment_value).split(',')
    data = ','.join(parts)
    importlib.import_module(str(data))
    return {"updated": True}
