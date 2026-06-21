# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
import os
import asyncio


async def BenchmarkTest18276(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return dotenv_value
    data = await fetch_payload()
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
