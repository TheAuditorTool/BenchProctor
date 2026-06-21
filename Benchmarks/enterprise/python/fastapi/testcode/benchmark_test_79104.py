# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest79104(request: Request):
    upload_name = (await request.form()).get('upload', '')
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
