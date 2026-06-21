# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest09382(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
