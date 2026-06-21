# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest28782(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
