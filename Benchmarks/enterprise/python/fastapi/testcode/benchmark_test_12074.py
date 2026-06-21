# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import asyncio
from app_runtime import db


async def BenchmarkTest12074(request: Request):
    referer_value = request.headers.get('referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = await fetch_payload()
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return {"updated": True}
