# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest75725(request: Request):
    user_id = request.query_params.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    eval(compile('_resp = requests.get(str(data))\nexec(_resp.text)', '<sink>', 'exec'))
    return {"updated": True}
