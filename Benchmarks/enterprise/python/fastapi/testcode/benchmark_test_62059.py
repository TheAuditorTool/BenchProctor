# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest62059(request: Request):
    query_array = request.query_params.get('items', '')
    data = str(query_array).replace('\x00', '')
    logging.info('User action: ' + str(data))
    return {"updated": True}
