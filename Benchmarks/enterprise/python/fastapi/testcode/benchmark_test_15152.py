# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest15152(request: Request):
    user_id = request.query_params.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
