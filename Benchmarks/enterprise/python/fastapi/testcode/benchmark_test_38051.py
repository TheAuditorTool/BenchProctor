# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from types import SimpleNamespace


async def BenchmarkTest38051(request: Request):
    host_value = request.headers.get('host', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return content
    return await _evasion_task()
