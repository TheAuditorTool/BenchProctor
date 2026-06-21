# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import importlib


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest04889():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = default_blank(graphql_var)
    async def _evasion_task():
        importlib.import_module(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
