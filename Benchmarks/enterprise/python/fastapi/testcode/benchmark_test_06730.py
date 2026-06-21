# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest06730(request: Request):
    user_id = request.query_params.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_OPTIONAL
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
