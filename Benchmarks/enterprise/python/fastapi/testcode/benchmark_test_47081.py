# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest47081(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = auth_header if auth_header else 'default'
    logging.info('User action: ' + str(data))
    return {"updated": True}
