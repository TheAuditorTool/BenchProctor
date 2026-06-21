# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest41935(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    logging.info('User action: ' + str(data))
    return {"updated": True}
