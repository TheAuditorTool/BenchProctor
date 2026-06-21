# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest15853(request: Request):
    referer_value = request.headers.get('referer', '')
    data = coalesce_blank(referer_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
