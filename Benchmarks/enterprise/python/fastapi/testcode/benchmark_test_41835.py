# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


def ensure_str(value):
    return str(value)

async def BenchmarkTest41835(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = ensure_str(header_value)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
