# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace
import tempfile
from app_runtime import db


async def BenchmarkTest16658(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
