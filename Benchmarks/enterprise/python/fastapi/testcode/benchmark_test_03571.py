# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest03571(request: Request):
    query_array = request.query_params.get('items', '')
    def normalize(value):
        return value.strip()
    data = normalize(query_array)
    logging.info('User action: ' + str(data))
    return {"updated": True}
