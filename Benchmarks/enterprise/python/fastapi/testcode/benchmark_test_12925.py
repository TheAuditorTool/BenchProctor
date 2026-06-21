# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest12925(request: Request):
    query_array = request.query_params.get('items', '')
    parts = []
    for token in str(query_array).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    logging.info('User action: ' + str(data))
    return {"updated": True}
