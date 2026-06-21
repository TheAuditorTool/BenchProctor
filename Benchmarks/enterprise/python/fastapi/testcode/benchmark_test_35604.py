# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import ast


async def BenchmarkTest35604(request: Request):
    upload_name = (await request.form()).get('upload', '')
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    os.remove(str(data))
    return {"updated": True}
