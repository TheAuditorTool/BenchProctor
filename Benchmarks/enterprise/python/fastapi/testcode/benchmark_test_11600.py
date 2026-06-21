# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast
import defusedxml.ElementTree


async def BenchmarkTest11600(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
