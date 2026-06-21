# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


def ensure_str(value):
    return str(value)

async def BenchmarkTest42711(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = ensure_str(multipart_value)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
