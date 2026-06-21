# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from fastapi import Form
import ast


async def BenchmarkTest74968(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
