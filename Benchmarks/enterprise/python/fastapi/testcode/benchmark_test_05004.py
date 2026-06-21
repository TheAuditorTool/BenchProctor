# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import ast
from app_runtime import db


async def BenchmarkTest05004(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    os.remove(str(data))
    return {"updated": True}
