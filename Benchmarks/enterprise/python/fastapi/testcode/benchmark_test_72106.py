# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


async def BenchmarkTest72106(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(multipart_value)).read()
    return {"updated": True}
