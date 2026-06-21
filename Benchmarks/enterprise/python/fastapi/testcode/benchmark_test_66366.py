# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest66366(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    os.remove(str(data))
    return {"updated": True}
