# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest07296(request: Request):
    origin_value = request.headers.get('origin', '')
    pending = list(str(origin_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    os.remove(str(data))
    return {"updated": True}
