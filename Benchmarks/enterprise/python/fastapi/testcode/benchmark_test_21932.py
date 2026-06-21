# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from fastapi import Form
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest21932(request: Request, field: str = Form('')):
    field_value = field
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = await fetch_payload()
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JSONResponse({'token': str(token)}, status_code=200)
