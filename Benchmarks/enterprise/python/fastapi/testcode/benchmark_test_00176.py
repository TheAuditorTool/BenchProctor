# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
import asyncio
import socket
from app_runtime import db


async def BenchmarkTest00176(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = await fetch_payload()
    if time.time() > 1000000000:
        s = socket.create_connection((str(data), 80))
        s.close()
    return {"updated": True}
