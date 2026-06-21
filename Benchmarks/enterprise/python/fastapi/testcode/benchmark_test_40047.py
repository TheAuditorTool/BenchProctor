# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import ast


async def BenchmarkTest40047(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    async def _evasion_task():
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return content
    return await _evasion_task()
