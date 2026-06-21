# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest06672(request: Request):
    user_id = request.query_params.get('id', '')
    data = user_id if user_id else 'default'
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
