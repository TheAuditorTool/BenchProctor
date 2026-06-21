# SPDX-License-Identifier: Apache-2.0
from flask import request
import os
import asyncio


def BenchmarkTest06262():
    user_id = request.args.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = asyncio.run(fetch_payload())
    async def _evasion_task():
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return content
    return asyncio.run(_evasion_task())
