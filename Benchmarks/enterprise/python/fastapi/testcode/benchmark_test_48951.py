# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import unquote


async def BenchmarkTest48951(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
