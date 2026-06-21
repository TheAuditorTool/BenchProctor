# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest08433(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    ctx = ssl.create_default_context()
    ctx.set_ciphers('aNULL')
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
