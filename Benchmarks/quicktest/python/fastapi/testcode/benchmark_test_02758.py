# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest02758(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    db.execute('UPDATE users SET name = ?', (str(data),))
    return {"updated": True}
