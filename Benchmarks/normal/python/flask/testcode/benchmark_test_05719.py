# SPDX-License-Identifier: Apache-2.0
import os
import asyncio
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest05719():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    async def _evasion_task():
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return content
    return asyncio.run(_evasion_task())
