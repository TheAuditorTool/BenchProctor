# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os
import asyncio


async def BenchmarkTest12528(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return dotenv_value
    data = await fetch_payload()
    logging.info('User action: ' + str(data))
    return {"updated": True}
