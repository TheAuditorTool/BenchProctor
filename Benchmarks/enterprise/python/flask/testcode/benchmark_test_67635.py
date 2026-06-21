# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import importlib
import sys


def ensure_str(value):
    return str(value)

def BenchmarkTest67635():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    async def _evasion_task():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
