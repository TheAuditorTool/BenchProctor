# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
from app_runtime import db


async def BenchmarkTest02358(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = await fetch_payload()
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
