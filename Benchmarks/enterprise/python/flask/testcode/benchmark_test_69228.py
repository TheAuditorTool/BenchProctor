# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import ast
import asyncio
from app_runtime import db


def BenchmarkTest69228():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    async def _evasion_task():
        requests.get(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
