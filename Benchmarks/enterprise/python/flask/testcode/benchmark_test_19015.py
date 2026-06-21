# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request
import ast
import asyncio


def BenchmarkTest19015():
    field_value = request.form.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    async def _evasion_task():
        return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
    return asyncio.run(_evasion_task())
