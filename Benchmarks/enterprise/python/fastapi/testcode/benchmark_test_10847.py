# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import ast
import defusedxml.ElementTree


async def BenchmarkTest10847(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
