# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import ast


async def BenchmarkTest06169(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    logging.info('User action: ' + str(data))
    return {"updated": True}
