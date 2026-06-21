# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest15473(request: Request):
    ua_value = request.headers.get('user-agent', '')
    logging.info('User action: ' + str(ua_value))
    return {"updated": True}
