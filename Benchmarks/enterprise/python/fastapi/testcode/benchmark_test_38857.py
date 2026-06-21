# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys
from types import SimpleNamespace


async def BenchmarkTest38857(request: Request):
    ua_value = request.headers.get('user-agent', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    await _evasion_task()
    return {"updated": True}
