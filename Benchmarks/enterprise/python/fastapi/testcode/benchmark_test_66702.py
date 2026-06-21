# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest66702(request: Request):
    referer_value = request.headers.get('referer', '')
    pending = list(str(referer_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    os.system('echo ' + str(data))
    return {"updated": True}
