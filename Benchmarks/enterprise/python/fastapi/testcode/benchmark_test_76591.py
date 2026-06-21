# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import unquote
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest76591(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
