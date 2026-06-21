# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
from app_runtime import db


async def BenchmarkTest81375(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = await fetch_payload()
    processed = data[:64]
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return {"updated": True}
