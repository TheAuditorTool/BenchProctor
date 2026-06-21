# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import ast


async def BenchmarkTest78501(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    os.unlink(checked_path)
    return {"updated": True}
