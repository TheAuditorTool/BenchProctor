# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import re
from fastapi import Form
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest35171(request: Request, field: str = Form('')):
    field_value = field
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = await fetch_payload()
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
