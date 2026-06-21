# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest58249(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % str(host_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
