# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest68874(request: Request):
    auth_header = request.headers.get('authorization', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
