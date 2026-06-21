# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest13213(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    ctx = ssl.create_default_context()
    ctx.set_ciphers('aNULL')
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
