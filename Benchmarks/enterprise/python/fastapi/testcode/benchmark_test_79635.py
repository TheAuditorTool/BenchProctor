# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def ensure_str(value):
    return str(value)

async def BenchmarkTest79635(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = ensure_str(header_value)
    async def _evasion_task():
        eval(str(data))
    await _evasion_task()
    return {"updated": True}
