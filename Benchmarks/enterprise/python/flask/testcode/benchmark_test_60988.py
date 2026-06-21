# SPDX-License-Identifier: Apache-2.0
from flask import request
import os
import asyncio


def BenchmarkTest60988():
    auth_header = request.headers.get('Authorization', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(auth_header)
    data = collected
    async def _evasion_task():
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return content
    return asyncio.run(_evasion_task())
