# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest00097(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    ctx = RequestContext(raw_body)
    data = ctx.payload
    checked_path = os.path.normpath(data)
    link_path = os.path.join('/var/app/data', str(checked_path))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
