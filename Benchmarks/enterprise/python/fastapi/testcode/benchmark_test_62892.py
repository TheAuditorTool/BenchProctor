# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def normalise_input(value):
    return value.strip()

async def BenchmarkTest62892(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = normalise_input(ua_value)
    async def _evasion_task():
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    await _evasion_task()
    return {"updated": True}
