# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
import ast


async def BenchmarkTest33604(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    try:
        data = str(ast.literal_eval(xml_value))
    except (ValueError, SyntaxError):
        data = xml_value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
