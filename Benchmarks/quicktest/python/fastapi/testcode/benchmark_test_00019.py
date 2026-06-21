# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


async def BenchmarkTest00019(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    pending = list(str(raw_body).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    importlib.import_module(str(data))
    return {"updated": True}
