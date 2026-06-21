# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest61895(request: Request):
    path_value = request.path_params.get('id', '')
    data = '%s' % (path_value,)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
