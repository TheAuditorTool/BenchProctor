# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from types import SimpleNamespace


async def BenchmarkTest04108(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
