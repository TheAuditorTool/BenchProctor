# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast
import urllib.request


async def BenchmarkTest37641(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
