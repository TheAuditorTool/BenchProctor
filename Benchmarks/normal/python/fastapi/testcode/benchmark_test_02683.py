# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest02683(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % str(auth_header)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
