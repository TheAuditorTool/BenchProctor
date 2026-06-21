# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import urllib.request


async def BenchmarkTest11436(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
