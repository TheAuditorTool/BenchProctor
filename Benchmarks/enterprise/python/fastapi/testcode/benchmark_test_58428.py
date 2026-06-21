# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def normalise_input(value):
    return value.strip()

async def BenchmarkTest58428(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = normalise_input(forwarded_ip)
    async def _evasion_task():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return await _evasion_task()
