# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request
import urllib.parse
import ssl


request_state: dict[str, str] = {}

async def BenchmarkTest61440(request: Request):
    user_id = request.query_params.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_OPTIONAL
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
