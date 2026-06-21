# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from starlette.responses import JSONResponse
import os
import asyncio


async def BenchmarkTest53333(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = await fetch_payload()
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
