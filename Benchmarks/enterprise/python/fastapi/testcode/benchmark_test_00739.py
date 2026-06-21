# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest00739(request: Request):
    origin_value = request.headers.get('origin', '')
    _resp = requests.get(str(origin_value))
    exec(_resp.text)
    return {"updated": True}
