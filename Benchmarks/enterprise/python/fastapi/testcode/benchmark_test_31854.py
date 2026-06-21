# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import ast


async def BenchmarkTest31854(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    logging.info('User action: ' + str(data))
    return {"updated": True}
