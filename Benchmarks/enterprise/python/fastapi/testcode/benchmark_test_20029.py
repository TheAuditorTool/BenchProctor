# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest20029(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header}'
    requests.get(str(data))
    return {"updated": True}
