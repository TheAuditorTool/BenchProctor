# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import unquote


async def BenchmarkTest27451(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    requests.get(str(data))
    return {"updated": True}
