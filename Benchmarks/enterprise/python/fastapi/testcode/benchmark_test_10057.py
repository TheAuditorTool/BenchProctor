# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import base64


async def BenchmarkTest10057(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    logging.info('User action: ' + str(data))
    return {"updated": True}
