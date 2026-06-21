# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import ast


async def BenchmarkTest73027(request: Request):
    upload_name = (await request.form()).get('upload', '')
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
