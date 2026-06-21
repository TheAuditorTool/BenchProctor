# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest09609(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return {"updated": True}
