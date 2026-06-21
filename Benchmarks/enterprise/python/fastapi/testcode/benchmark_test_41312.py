# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest41312(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    logging.info('User action: ' + str(forwarded_ip))
    return {"updated": True}
