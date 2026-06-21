# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
from app_runtime import db


async def BenchmarkTest10771(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data, _sep, _rest = str(comment_value).partition('\x00')
    importlib.import_module(str(data))
    return {"updated": True}
