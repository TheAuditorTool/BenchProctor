# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import asyncio


def relay_value(value):
    return value

def BenchmarkTest34702():
    field_value = request.form.get('field', '')
    data = relay_value(field_value)
    async def _evasion_task():
        os.system('echo ' + str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
