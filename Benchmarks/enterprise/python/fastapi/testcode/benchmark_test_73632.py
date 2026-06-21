# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def normalise_input(value):
    return value.strip()

async def BenchmarkTest73632(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = normalise_input(ua_value)
    async def _evasion_task():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return await _evasion_task()
