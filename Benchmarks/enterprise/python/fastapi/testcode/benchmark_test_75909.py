# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import os
import asyncio


async def BenchmarkTest75909(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = await fetch_payload()
    if os.environ.get("APP_ENV", "production") != "test":
        yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
