# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest06544(request: Request):
    user_id = request.query_params.get('id', '')
    data = user_id if user_id else 'default'
    requests.get(str(data))
    return {"updated": True}
