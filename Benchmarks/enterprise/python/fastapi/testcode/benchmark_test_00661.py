# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest00661(request: Request):
    path_value = request.path_params.get('id', '')
    ctx = RequestContext(path_value)
    data = ctx.payload
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
