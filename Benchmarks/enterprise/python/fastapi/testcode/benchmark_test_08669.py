# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


async def BenchmarkTest08669(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    pending = list(str(header_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    importlib.import_module(str(data))
    return {"updated": True}
