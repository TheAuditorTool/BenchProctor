# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
from app_runtime import auth_check


async def BenchmarkTest10530(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    async def fetch_payload():
        await asyncio.sleep(0)
        return yaml_value
    data = await fetch_payload()
    auth_check('user', data)
    return {"updated": True}
