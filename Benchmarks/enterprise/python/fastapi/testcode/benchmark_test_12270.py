# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest12270(request: Request):
    query_array = request.query_params.get('items', '')
    prefix = ''
    data = prefix + str(query_array)
    logging.info('User action: ' + str(data))
    return {"updated": True}
