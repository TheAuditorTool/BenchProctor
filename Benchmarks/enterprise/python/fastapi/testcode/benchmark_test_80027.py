# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import asyncio
from app_runtime import db


async def BenchmarkTest80027(request: Request):
    auth_header = request.headers.get('authorization', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = await fetch_payload()
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
