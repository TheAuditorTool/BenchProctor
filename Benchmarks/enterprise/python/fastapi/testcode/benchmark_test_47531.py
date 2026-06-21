# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest47531(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
