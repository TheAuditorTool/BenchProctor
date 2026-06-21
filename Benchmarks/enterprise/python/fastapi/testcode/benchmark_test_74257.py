# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
import ast


async def BenchmarkTest74257(request: Request):
    upload_name = (await request.form()).get('upload', '')
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
