# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest10407(request: Request):
    user_id = request.query_params.get('id', '')
    data = str(user_id).replace('\x00', '')
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
