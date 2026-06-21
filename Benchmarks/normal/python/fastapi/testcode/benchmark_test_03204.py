# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


async def BenchmarkTest03204(request: Request):
    referer_value = request.headers.get('referer', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(referer_value)
    data = collected
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
