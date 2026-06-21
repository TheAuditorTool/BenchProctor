# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form
import ast


async def BenchmarkTest38114(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    eval(compile("with open('/var/uploads/' + str(data), 'wb') as fh:\n    fh.write(b'data')", '<sink>', 'exec'))
    return {"updated": True}
