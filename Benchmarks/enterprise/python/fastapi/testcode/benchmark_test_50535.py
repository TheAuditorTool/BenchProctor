# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest50535(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
