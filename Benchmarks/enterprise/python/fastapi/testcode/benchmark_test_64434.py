# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest64434(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(xml_value)
    data = collected
    eval(compile('eval(str(data))', '<sink>', 'exec'))
    return {"updated": True}
