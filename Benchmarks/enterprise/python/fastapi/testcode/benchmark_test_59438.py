# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


async def BenchmarkTest59438(request: Request):
    origin_value = request.headers.get('origin', '')
    pending = list(str(origin_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
