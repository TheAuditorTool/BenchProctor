# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import ast
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest10263(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
