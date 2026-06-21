# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest24650(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    pending = list(str(xml_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    int(str(data))
    return {"updated": True}
