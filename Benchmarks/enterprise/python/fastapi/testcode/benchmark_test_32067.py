# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
import asyncio
import importlib
from app_runtime import db


async def BenchmarkTest32067(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = await fetch_payload()
    if time.time() > 1000000000:
        importlib.import_module(str(data))
    return {"updated": True}
