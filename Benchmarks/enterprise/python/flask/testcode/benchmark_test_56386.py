# SPDX-License-Identifier: Apache-2.0
from flask import request
import asyncio


def relay_value(value):
    return value

def BenchmarkTest56386():
    ua_value = request.headers.get('User-Agent', '')
    data = relay_value(ua_value)
    async def _evasion_task():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return asyncio.run(_evasion_task())
