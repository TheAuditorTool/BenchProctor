# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import ast


async def BenchmarkTest58253(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
