# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
import urllib.request
import urllib.parse
import ssl


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest48041(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
