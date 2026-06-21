# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest01710(request: Request):
    path_value = request.path_params.get('id', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(path_value)}, verify=True)
    return {"updated": True}
