# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import urllib.request


async def BenchmarkTest70836(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
