# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import ast


async def BenchmarkTest76258(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    try:
        data = str(ast.literal_eval(yaml_value))
    except (ValueError, SyntaxError):
        data = yaml_value
    logging.info('User action: ' + str(data))
    return {"updated": True}
