# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import runpy
from types import SimpleNamespace


async def BenchmarkTest32111(request: Request):
    referer_value = request.headers.get('referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    await _evasion_task()
    return {"updated": True}
