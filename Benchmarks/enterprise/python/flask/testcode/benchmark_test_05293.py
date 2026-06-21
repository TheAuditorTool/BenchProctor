# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import ast
import asyncio


def BenchmarkTest05293(path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    async def _evasion_task():
        return render_template_string(data)
    return asyncio.run(_evasion_task())
