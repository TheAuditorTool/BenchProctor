# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
import ast


async def BenchmarkTest50505(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
