# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import urllib.request
import urllib.parse
import ssl
from types import SimpleNamespace


async def BenchmarkTest22803(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
