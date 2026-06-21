# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import ast


async def BenchmarkTest01993(request: Request):
    upload_name = (await request.form()).get('upload', '')
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    globals()['counter'] = int(data)
    return {"updated": True}
