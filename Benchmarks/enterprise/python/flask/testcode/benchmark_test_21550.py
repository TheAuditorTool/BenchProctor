# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import asyncio


def BenchmarkTest21550(path_param):
    path_value = path_param
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    async def _evasion_task():
        with open('/var/app/data/' + str(data), 'w') as fh:
            fh.write('data')
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
