# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import ast
from app_runtime import db


async def BenchmarkTest62803(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
