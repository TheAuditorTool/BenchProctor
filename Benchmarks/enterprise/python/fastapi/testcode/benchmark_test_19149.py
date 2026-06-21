# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import urllib.request


async def BenchmarkTest19149(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
