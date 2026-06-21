# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest52716(request: Request):
    query_array = request.query_params.get('items', '')
    kind = 'json' if str(query_array).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = query_array
            data = parsed
        case _:
            data = query_array
    logging.info('User action: ' + str(data))
    return {"updated": True}
