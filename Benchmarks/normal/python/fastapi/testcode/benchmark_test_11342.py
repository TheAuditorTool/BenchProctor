# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os
import urllib.request
import urllib.parse
import ssl


request_state: dict[str, str] = {}

async def BenchmarkTest11342(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    _cipher = Fernet(os.environ['DATA_ENC_KEY'].encode())
    ctx = ssl.create_default_context()
    ctx.set_ciphers('aNULL')
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
