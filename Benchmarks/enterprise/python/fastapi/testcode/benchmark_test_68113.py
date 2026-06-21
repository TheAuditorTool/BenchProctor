# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace
import defusedxml.ElementTree
from app_runtime import db


async def BenchmarkTest68113(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
