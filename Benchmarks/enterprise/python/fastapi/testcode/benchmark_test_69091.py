# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import ast
from app_runtime import db


async def BenchmarkTest69091(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
