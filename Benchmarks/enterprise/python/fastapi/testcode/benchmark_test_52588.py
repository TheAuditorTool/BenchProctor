# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest52588(request: Request):
    origin_value = request.headers.get('origin', '')
    reader = make_reader(origin_value)
    data = reader()
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
