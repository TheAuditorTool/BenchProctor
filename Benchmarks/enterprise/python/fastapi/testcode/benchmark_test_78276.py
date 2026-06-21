# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


def normalise_input(value):
    return value.strip()

async def BenchmarkTest78276(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = normalise_input(ua_value)
    async def _evasion_task():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    await _evasion_task()
    return {"updated": True}
