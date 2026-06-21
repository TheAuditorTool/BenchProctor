# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
from types import SimpleNamespace


async def BenchmarkTest69900(request: Request):
    upload_name = (await request.form()).get('upload', '')
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
