# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time
import ast


async def BenchmarkTest02054(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return {"updated": True}
