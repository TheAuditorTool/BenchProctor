# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest16134(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % str(user_id)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
