# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest11332(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(xml_value)
    data = collected
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
