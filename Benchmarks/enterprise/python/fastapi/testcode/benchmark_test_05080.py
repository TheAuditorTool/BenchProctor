# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import time
import asyncio
from app_runtime import db


async def BenchmarkTest05080(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = await fetch_payload()
    if time.time() > 1000000000:
        subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
