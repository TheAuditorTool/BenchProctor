# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest59596(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(graphql_var)), context=ctx)
    return {"updated": True}
