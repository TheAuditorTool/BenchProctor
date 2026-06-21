# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os
import ast


async def BenchmarkTest73351(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    try:
        data = str(ast.literal_eval(dotenv_value))
    except (ValueError, SyntaxError):
        data = dotenv_value
    logging.info('User action: ' + str(data))
    return {"updated": True}
