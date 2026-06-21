# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import asyncio


async def BenchmarkTest12896(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    async def fetch_payload():
        await asyncio.sleep(0)
        return yaml_value
    data = await fetch_payload()
    logging.info('User action: ' + str(data))
    return {"updated": True}
