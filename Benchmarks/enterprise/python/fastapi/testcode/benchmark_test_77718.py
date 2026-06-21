# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import ast
from app_runtime import db


async def BenchmarkTest77718(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
