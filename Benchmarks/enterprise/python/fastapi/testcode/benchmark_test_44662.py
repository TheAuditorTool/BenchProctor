# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import requests


async def BenchmarkTest44662(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
