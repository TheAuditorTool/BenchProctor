# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from fastapi import Form
from starlette.responses import JSONResponse
import asyncio
import subprocess


async def BenchmarkTest00279(request: Request, field: str = Form('')):
    field_value = field
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = await fetch_payload()
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return {"updated": True}
