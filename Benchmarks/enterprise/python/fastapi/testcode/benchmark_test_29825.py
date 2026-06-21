# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest29825(request: Request):
    host_value = request.headers.get('host', '')
    data = ' '.join(str(host_value).split())
    logging.info('User action: ' + str(data))
    return {"updated": True}
