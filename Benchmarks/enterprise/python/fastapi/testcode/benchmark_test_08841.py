# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
from app_runtime import auth_check


async def BenchmarkTest08841(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return multipart_value
    data = await fetch_payload()
    auth_check('user', data)
    return {"updated": True}
