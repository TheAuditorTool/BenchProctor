# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest42403(request: Request):
    referer_value = request.headers.get('referer', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(referer_value)
    data = collected
    request.session['user'] = str(data)
    return {"updated": True}
