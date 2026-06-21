# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


request_state: dict[str, str] = {}

async def BenchmarkTest09276(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
