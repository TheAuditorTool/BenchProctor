# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
import tempfile
from app_runtime import db


async def BenchmarkTest75084(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = await fetch_payload()
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
