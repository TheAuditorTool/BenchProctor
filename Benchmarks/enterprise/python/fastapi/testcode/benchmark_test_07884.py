# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest07884(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    await _evasion_task()
    return {"updated": True}
