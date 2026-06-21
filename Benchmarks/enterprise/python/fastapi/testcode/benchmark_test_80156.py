# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest80156(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(raw_body)
    data = collected
    def _primary():
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
