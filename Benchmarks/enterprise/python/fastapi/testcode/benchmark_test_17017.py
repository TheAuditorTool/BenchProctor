# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast


async def BenchmarkTest17017(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    async def _evasion_task():
        eval(str(data))
    await _evasion_task()
    return {"updated": True}
