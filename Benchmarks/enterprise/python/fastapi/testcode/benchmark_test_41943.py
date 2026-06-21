# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import ast
import subprocess
from app_runtime import db


async def BenchmarkTest41943(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    async def _evasion_task():
        subprocess.run([str(data), '--status'], shell=False)
    await _evasion_task()
    return {"updated": True}
