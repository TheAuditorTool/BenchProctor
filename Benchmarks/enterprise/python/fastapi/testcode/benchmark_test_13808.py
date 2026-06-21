# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest13808(request: Request):
    referer_value = request.headers.get('referer', '')
    _resp = requests.get(str(referer_value))
    exec(_resp.text)
    return {"updated": True}
