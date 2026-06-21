# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest71031(request: Request):
    host_value = request.headers.get('host', '')
    data = '{}'.format(host_value)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
