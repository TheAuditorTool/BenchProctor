# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import ast
import asyncio


def BenchmarkTest06856():
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    async def _evasion_task():
        os.system('echo ' + str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
