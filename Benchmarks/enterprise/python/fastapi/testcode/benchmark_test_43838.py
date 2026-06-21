# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest43838(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(raw_body)
    data = collected
    processed = data[:64]
    request.session['data'] = str(processed)
    return {"updated": True}
