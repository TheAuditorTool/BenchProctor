# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
from types import SimpleNamespace


async def BenchmarkTest80418(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
