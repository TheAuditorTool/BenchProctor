# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import asyncio
from app_runtime import db


async def BenchmarkTest50508(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = await fetch_payload()
    async def _evasion_task():
        os.unlink('/var/app/data/' + str(data))
    await _evasion_task()
    return {"updated": True}
