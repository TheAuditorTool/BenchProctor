# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest16322(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
