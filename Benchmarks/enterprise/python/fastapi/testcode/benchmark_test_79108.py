# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json


async def BenchmarkTest79108(request: Request):
    ua_value = request.headers.get('user-agent', '')
    pending = list(str(ua_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    yaml.safe_load(data)
    return {"updated": True}
