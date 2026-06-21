# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import urllib.request


async def BenchmarkTest01144(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
