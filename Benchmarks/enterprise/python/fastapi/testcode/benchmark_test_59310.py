# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import ast
import importlib
from app_runtime import db


async def BenchmarkTest59310(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    if os.environ.get("APP_ENV", "production") != "test":
        importlib.import_module(str(data))
    return {"updated": True}
