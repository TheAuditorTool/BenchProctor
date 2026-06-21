# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
from app_runtime import db


async def BenchmarkTest70363(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '{}'.format(comment_value)
    importlib.import_module(str(data))
    return {"updated": True}
