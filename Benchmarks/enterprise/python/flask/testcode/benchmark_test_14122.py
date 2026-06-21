# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
import ast
import asyncio


def BenchmarkTest14122():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    async def _evasion_task():
        return Markup('<div>' + str(data) + '</div>')
    return asyncio.run(_evasion_task())
