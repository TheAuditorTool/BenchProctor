# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import unquote


async def BenchmarkTest47559(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
