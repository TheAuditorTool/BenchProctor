# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest67823(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
