# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest02089(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return {"updated": True}
