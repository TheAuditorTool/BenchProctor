# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import ast
from app_runtime import db


async def BenchmarkTest74850(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
