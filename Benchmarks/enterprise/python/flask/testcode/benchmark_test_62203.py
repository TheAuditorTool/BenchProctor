# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
import asyncio


def BenchmarkTest62203():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    async def _evasion_task():
        eval(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
