# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import runpy
from types import SimpleNamespace


async def BenchmarkTest42815(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    await _evasion_task()
    return {"updated": True}
