# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import ast
import asyncio
import subprocess
from app_runtime import db


def BenchmarkTest50157():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    async def _evasion_task():
        subprocess.run([str(data), '--status'], shell=False)
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
