# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json
import time
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest41642(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
