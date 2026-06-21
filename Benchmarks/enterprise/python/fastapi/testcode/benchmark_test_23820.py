# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def normalise_input(value):
    return value.strip()

async def BenchmarkTest23820(request: Request):
    referer_value = request.headers.get('referer', '')
    data = normalise_input(referer_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
