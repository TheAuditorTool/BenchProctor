# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest62915(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = '{}'.format(header_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
