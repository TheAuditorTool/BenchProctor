# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import ast


async def BenchmarkTest76517(request: Request):
    origin_value = request.headers.get('origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    logging.info('User action: ' + str(data))
    return {"updated": True}
