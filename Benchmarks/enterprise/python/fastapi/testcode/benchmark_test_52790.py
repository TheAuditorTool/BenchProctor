# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import sys


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest52790(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    ctx = RequestContext(argv_value)
    data = ctx.payload
    processed = data[:64]
    os.unlink('/var/app/data/' + str(processed))
    return {"updated": True}
