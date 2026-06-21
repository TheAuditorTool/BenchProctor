# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest59393(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = default_blank(ua_value)
    async def _evasion_task():
        eval(str(data))
    await _evasion_task()
    return {"updated": True}
