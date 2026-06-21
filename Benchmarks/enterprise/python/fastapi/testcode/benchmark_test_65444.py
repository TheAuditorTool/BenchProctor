# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest65444(request: Request):
    referer_value = request.headers.get('referer', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(referer_value)}, verify=True)
    return {"updated": True}
