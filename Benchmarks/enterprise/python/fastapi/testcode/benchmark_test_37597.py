# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest37597(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    reader = make_reader(header_value)
    data = reader()
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
