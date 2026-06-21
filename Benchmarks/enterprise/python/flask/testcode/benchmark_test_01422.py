# SPDX-License-Identifier: Apache-2.0
from flask import request
import os
import asyncio


def BenchmarkTest01422():
    user_id = request.args.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = asyncio.run(fetch_payload())
    async def _evasion_task():
        link_path = os.path.join('/var/app/data', str(data))
        target = os.readlink(link_path)
        with open(target, 'r') as fh:
            content = fh.read()
        return content
    return asyncio.run(_evasion_task())
