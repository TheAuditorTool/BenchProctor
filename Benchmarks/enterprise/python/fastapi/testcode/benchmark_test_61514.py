# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from types import SimpleNamespace


async def BenchmarkTest61514(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        eval(str(data))
    await _evasion_task()
    return {"updated": True}
