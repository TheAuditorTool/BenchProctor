# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def to_text(value):
    return str(value).strip()

async def BenchmarkTest07688(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = to_text(ua_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
