# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest08277(request: Request):
    query_array = request.query_params.get('items', '')
    if query_array:
        data = query_array
    else:
        data = ''
    logging.info('User action: ' + str(data))
    return {"updated": True}
