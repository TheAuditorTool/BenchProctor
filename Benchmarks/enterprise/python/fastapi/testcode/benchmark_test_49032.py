# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from types import SimpleNamespace
from app_runtime import auth_check


async def BenchmarkTest49032(request: Request):
    referer_value = request.headers.get('referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return {"updated": True}
