# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest73615(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
