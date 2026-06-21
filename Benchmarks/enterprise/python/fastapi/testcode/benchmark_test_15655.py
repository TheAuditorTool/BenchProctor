# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os
import urllib.request
import urllib.parse
import ssl


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest15655(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = coalesce_blank(forwarded_ip)
    _cipher = Fernet(os.environ['DATA_ENC_KEY'].encode())
    ctx = ssl.create_default_context()
    ctx.set_ciphers('aNULL')
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
