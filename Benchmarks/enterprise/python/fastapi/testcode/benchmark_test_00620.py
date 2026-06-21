# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import ast
import ctypes
from app_runtime import db


async def BenchmarkTest00620(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    processed = data[:64]
    requested = int(str(processed))
    wrapped = ctypes.c_int32(requested + 1).value
    return JSONResponse({'wrapped': wrapped}, status_code=200)
