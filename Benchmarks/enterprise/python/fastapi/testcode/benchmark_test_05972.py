# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest05972(request: Request):
    origin_value = request.headers.get('origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    requests.get(str(data))
    return {"updated": True}
