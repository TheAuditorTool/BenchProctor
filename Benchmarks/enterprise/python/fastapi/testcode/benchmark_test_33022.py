# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest33022(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % str(user_id)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
