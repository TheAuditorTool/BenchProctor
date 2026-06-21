# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
import asyncio


def BenchmarkTest32314():
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    async def _evasion_task():
        eval(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
