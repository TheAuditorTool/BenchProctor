# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest02651(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    logging.info('User action: ' + str(data))
    return {"updated": True}
