# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import ast
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest00216(request: Request):
    origin_value = request.headers.get('origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
