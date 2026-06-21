# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest15557(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_OPTIONAL
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
