# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest26134(request: Request):
    host_value = request.headers.get('host', '')
    reader = make_reader(host_value)
    data = reader()
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
