# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import asyncio
import runpy


def coalesce_blank(value):
    return value or ''

def BenchmarkTest44305(path_param):
    path_value = path_param
    data = coalesce_blank(path_value)
    async def _evasion_task():
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
