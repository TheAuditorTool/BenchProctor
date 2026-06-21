# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse
import asyncio


async def BenchmarkTest19675(request: Request):
    upload_name = (await request.form()).get('upload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = await fetch_payload()
    async def _evasion_task():
        return HTMLResponse('<script src="' + str(data) + '"></script>')
    return await _evasion_task()
