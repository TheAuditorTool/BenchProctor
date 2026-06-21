# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time
import ast


async def BenchmarkTest37584(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    try:
        data = str(ast.literal_eval(xml_value))
    except (ValueError, SyntaxError):
        data = xml_value
    if time.time() > 1000000000:
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return content
    return {"updated": True}
