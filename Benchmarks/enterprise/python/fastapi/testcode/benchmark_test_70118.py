# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def to_text(value):
    return str(value).strip()

async def BenchmarkTest70118(request: Request):
    host_value = request.headers.get('host', '')
    data = to_text(host_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
