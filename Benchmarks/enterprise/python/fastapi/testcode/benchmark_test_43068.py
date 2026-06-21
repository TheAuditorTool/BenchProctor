# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest43068(request: Request):
    auth_header = request.headers.get('authorization', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(auth_header)
    data = collected
    request.session['data'] = str(data)
    return {"updated": True}
