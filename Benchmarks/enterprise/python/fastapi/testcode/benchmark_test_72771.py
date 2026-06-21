# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import asyncio
from app_runtime import db


_shared_counter_lock = threading.Lock()

async def BenchmarkTest72771(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = await fetch_payload()
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
