# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import unquote


async def BenchmarkTest69142(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
