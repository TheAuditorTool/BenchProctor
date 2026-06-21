# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest77045(request: Request):
    auth_header = request.headers.get('authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
