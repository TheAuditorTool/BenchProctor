# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest22769(request: Request):
    user_id = request.query_params.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(user_id)
    data = collected
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
