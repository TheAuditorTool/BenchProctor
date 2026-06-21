# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os
import asyncio


async def BenchmarkTest26310(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = await fetch_payload()
    logging.info('User action: ' + str(data))
    return {"updated": True}
