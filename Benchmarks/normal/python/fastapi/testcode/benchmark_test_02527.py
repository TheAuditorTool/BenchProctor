# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest02527(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    requests.get(str(data))
    return {"updated": True}
