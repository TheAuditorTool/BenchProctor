# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest26155(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
