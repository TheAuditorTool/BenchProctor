# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import asyncio
from app_runtime import db


async def BenchmarkTest70628(request: Request, field: str = Form('')):
    field_value = field
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = await fetch_payload()
    db.execute('UPDATE users SET name = ?', (str(data),))
    return {"updated": True}
