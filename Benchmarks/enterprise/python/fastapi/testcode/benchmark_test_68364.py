# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest68364(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(xml_value)
    data = collected
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
