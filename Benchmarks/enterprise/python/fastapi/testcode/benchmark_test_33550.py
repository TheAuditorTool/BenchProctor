# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import urllib.request


async def BenchmarkTest33550(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data, _sep, _rest = str(graphql_var).partition('\x00')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
