# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os
import ast


async def BenchmarkTest00796(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    logging.info('User action: ' + str(data))
    return {"updated": True}
