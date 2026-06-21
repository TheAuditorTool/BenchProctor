# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest03468(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % (host_value,)
    logging.info('User action: ' + str(data))
    return {"updated": True}
