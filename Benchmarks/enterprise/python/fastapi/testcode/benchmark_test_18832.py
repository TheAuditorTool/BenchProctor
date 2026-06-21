# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest18832(request: Request):
    user_id = request.query_params.get('id', '')
    data = ' '.join(str(user_id).split())
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
