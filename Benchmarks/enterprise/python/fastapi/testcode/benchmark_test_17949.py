# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest17949(request: Request):
    host_value = request.headers.get('host', '')
    pending = list(str(host_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
