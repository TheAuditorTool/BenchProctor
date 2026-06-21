# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


async def BenchmarkTest27047(request: Request):
    path_value = request.path_params.get('id', '')
    data, _sep, _rest = str(path_value).partition('\x00')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
