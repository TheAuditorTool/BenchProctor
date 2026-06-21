# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import ast
import asyncio
import importlib
import sys
from app_runtime import db


def BenchmarkTest76932():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    async def _evasion_task():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
