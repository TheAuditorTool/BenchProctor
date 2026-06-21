# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest52810(request: Request):
    path_value = request.path_params.get('id', '')
    pending = list(str(path_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    json.loads(data)
    return {"updated": True}
