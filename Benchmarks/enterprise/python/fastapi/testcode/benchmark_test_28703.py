# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest28703(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = default_blank(header_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
