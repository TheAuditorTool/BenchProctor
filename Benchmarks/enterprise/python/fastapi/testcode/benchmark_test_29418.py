# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import asyncio
from app_runtime import db


async def BenchmarkTest29418(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return multipart_value
    data = await fetch_payload()
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
