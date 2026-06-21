# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
import asyncio


def BenchmarkTest79949():
    upload_name = request.files['upload'].filename
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    async def _evasion_task():
        eval(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
