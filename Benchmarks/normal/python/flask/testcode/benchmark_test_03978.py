# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import ast
import asyncio


def BenchmarkTest03978():
    raw_body = request.get_data(as_text=True)
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    async def _evasion_task():
        _resp = requests.get(str(data))
        exec(_resp.text)
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
