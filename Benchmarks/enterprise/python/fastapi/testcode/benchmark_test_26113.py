# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from types import SimpleNamespace
from app_runtime import auth_check


async def BenchmarkTest26113(request: Request):
    host_value = request.headers.get('host', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return {"updated": True}
