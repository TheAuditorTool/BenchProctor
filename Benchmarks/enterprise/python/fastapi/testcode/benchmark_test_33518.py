# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


async def BenchmarkTest33518(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = upload_name if upload_name else 'default'
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
