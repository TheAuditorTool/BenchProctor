# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest67228(request: Request):
    user_id = request.query_params.get('id', '')
    data = user_id if user_id else 'default'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
