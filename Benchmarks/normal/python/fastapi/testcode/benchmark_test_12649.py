# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from types import SimpleNamespace


async def BenchmarkTest12649(request: Request):
    origin_value = request.headers.get('origin', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    yaml.safe_load(data)
    return {"updated": True}
