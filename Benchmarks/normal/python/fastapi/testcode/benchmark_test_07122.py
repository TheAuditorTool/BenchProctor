# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest07122(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    logging.info('User action: ' + str(raw_body))
    return {"updated": True}
