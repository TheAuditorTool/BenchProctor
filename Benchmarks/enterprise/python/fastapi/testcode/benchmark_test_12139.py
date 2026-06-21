# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest12139(request: Request):
    path_value = request.path_params.get('id', '')
    prefix = ''
    data = prefix + str(path_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
