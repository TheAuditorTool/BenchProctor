# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest09120(request: Request):
    user_id = request.query_params.get('id', '')
    requests.post('https://api.prod.internal/data', data=str(user_id), verify=True)
    return {"updated": True}
