# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest80155(request: Request):
    user_id = request.query_params.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
