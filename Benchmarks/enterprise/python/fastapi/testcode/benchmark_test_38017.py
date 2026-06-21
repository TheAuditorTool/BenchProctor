# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys
from app_runtime import db


async def BenchmarkTest38017(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(comment_value).split(',')
    data = ','.join(parts)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
