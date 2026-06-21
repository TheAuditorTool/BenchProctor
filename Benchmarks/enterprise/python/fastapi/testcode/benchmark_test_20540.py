# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest20540(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id}'
    requests.get(str(data))
    return {"updated": True}
