# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest28785(request: Request, field: str = Form('')):
    field_value = field
    ctx = RequestContext(field_value)
    data = ctx.payload
    processed = data[:64]
    link_path = os.path.join('/var/app/data', str(processed))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
