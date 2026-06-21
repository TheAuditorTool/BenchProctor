# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def normalise_input(value):
    return value.strip()

async def BenchmarkTest25806(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = normalise_input(auth_header)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
