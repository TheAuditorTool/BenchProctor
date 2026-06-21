# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from types import SimpleNamespace


async def BenchmarkTest74977(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    yaml.safe_load(data)
    return {"updated": True}
