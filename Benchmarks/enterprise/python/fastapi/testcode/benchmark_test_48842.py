# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace
from app_runtime import auth_check


async def BenchmarkTest48842(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    auth_check('user', data)
    return {"updated": True}
