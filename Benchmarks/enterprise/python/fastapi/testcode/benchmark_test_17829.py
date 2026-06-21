# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from fastapi import Form
import asyncio


async def BenchmarkTest17829(request: Request, field: str = Form('')):
    field_value = field
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = await fetch_payload()
    logging.info('User action: ' + str(data))
    return {"updated": True}
