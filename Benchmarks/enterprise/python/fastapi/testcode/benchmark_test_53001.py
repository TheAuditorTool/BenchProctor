# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest53001(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    logging.info('User action: ' + str(header_value))
    return {"updated": True}
