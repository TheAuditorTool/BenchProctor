# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest32309(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    eval(compile("db.execute('SELECT * FROM users WHERE id = ' + str(data))", '<sink>', 'exec'))
    return {"updated": True}
