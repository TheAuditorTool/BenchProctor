# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest79882(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    parts = str(forwarded_ip).split(',')
    data = ','.join(parts)
    logging.info('User action: ' + str(data))
    return {"updated": True}
