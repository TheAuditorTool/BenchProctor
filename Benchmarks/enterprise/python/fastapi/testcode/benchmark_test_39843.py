# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import ast


async def BenchmarkTest39843(request: Request):
    query_array = request.query_params.get('items', '')
    try:
        data = str(ast.literal_eval(query_array))
    except (ValueError, SyntaxError):
        data = query_array
    logging.info('User action: ' + str(data))
    return {"updated": True}
