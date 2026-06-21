# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest50231(request: Request):
    host_value = request.headers.get('host', '')
    data = default_blank(host_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
