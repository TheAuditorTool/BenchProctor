# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


async def BenchmarkTest27813(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    pending = list(str(forwarded_ip).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    yaml.safe_load(data)
    return {"updated": True}
