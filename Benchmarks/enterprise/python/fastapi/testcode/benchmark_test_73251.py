# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
from types import SimpleNamespace


async def BenchmarkTest73251(request: Request):
    path_value = request.path_params.get('id', '')
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        exec(str(data))
    return {"updated": True}
