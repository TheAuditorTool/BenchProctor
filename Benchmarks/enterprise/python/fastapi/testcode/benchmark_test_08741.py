# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import asyncio


async def BenchmarkTest08741(request: Request):
    user_id = request.query_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = await fetch_payload()
    eval(compile('yaml.load(data, Loader=yaml.UnsafeLoader)', '<sink>', 'exec'))
    return {"updated": True}
