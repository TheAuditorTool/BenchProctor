# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest62427(request: Request):
    auth_header = request.headers.get('authorization', '')
    logging.info('User action: ' + str(auth_header))
    return {"updated": True}
