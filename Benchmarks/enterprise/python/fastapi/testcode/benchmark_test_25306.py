# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest25306(request: Request):
    auth_header = request.headers.get('authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    requests.get(str(data))
    return {"updated": True}
