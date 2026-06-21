# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest00430(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    parts = str(graphql_var).split(',')
    data = ','.join(parts)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
