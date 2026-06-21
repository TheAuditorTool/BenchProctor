# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest32743(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % str(host_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return {"updated": True}
