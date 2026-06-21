# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import ast
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest09014(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    try:
        data = str(ast.literal_eval(xml_value))
    except (ValueError, SyntaxError):
        data = xml_value
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
