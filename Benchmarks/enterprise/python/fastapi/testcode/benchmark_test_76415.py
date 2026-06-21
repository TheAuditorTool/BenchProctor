# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


async def BenchmarkTest76415(request: Request):
    path_value = request.path_params.get('id', '')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(path_value)).read()
    return {"updated": True}
