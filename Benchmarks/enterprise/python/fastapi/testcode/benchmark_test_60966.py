# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast


async def BenchmarkTest60966(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
