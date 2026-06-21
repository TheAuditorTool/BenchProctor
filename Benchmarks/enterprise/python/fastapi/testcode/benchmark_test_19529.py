# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest19529(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
