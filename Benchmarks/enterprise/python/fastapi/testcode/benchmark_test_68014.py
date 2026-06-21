# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def relay_value(value):
    return value

async def BenchmarkTest68014(request: Request):
    host_value = request.headers.get('host', '')
    data = relay_value(host_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
