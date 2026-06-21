# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from types import SimpleNamespace


async def BenchmarkTest41774(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    globals()['counter'] = int(processed)
    return {"updated": True}
