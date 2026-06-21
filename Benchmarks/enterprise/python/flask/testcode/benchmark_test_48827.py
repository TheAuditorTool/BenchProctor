# SPDX-License-Identifier: Apache-2.0
from flask import request
import asyncio


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest48827():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = default_blank(forwarded_ip)
    async def _evasion_task():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return asyncio.run(_evasion_task())
