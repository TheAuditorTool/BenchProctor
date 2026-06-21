# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest72451(request: Request):
    host_value = request.headers.get('host', '')
    logging.info('User action: ' + str(host_value))
    return {"updated": True}
