# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import ast


async def BenchmarkTest79946(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    try:
        data = str(ast.literal_eval(prop_value))
    except (ValueError, SyntaxError):
        data = prop_value
    logging.info('User action: ' + str(data))
    return {"updated": True}
