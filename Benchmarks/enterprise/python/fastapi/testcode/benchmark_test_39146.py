# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import asyncio
from app_runtime import db


async def BenchmarkTest39146(request: Request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    async def fetch_payload():
        await asyncio.sleep(0)
        return secret_value
    data = await fetch_payload()
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    db.connect(host='localhost', user='app', password=processed)
    return {"updated": True}
