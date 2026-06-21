# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def relay_value(value):
    return value

async def BenchmarkTest30010(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = relay_value(ua_value)
    async def _evasion_task():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return await _evasion_task()
