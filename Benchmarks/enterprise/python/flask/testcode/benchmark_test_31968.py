# SPDX-License-Identifier: Apache-2.0
from flask import request
import asyncio


def normalise_input(value):
    return value.strip()

def BenchmarkTest31968():
    ua_value = request.headers.get('User-Agent', '')
    data = normalise_input(ua_value)
    async def _evasion_task():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return asyncio.run(_evasion_task())
