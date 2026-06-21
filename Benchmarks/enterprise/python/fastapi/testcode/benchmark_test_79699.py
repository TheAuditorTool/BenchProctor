# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from types import SimpleNamespace
import subprocess


async def BenchmarkTest79699(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        subprocess.run([str(data), '--status'], shell=False)
    await _evasion_task()
    return {"updated": True}
