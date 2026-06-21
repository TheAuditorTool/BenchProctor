# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest65809(request: Request):
    ua_value = request.headers.get('user-agent', '')
    reader = make_reader(ua_value)
    data = reader()
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
