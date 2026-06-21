# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest31103(request: Request):
    query_array = request.query_params.get('items', '')
    data, _sep, _rest = str(query_array).partition('\x00')
    logging.info('User action: ' + str(data))
    return {"updated": True}
