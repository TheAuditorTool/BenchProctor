# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import ast


async def BenchmarkTest21058(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    try:
        data = str(ast.literal_eval(xml_value))
    except (ValueError, SyntaxError):
        data = xml_value
    eval(compile("with open('/var/uploads/' + str(data), 'wb') as fh:\n    fh.write(b'data')", '<sink>', 'exec'))
    return {"updated": True}
