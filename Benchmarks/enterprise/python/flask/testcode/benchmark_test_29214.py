# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import importlib


def normalise_input(value):
    return value.strip()

def BenchmarkTest29214():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    async def _evasion_task():
        importlib.import_module(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
