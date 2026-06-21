# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import asyncio
from app_runtime import db


async def BenchmarkTest70307(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return profile_value
    data = await fetch_payload()
    processed = data[:64]
    os.unlink('/var/app/data/' + str(processed))
    return {"updated": True}
