# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest73211(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    reader = make_reader(header_value)
    data = reader()
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
