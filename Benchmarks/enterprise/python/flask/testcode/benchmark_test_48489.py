# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
import ast
import asyncio


def BenchmarkTest48489():
    origin_value = request.headers.get('Origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    async def _evasion_task():
        return Markup('<img src="' + str(data) + '">')
    return asyncio.run(_evasion_task())
