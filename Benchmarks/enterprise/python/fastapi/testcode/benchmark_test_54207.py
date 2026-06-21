# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest54207(request: Request):
    user_id = request.query_params.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    processed = data[:64]
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return {"updated": True}
