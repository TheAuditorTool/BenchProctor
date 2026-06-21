# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import runpy
from types import SimpleNamespace


def BenchmarkTest80556():
    field_value = request.form.get('field', '')
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
