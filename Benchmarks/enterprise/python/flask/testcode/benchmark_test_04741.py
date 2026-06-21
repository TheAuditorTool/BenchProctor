# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def coalesce_blank(value):
    return value or ''

def BenchmarkTest04741():
    multipart_value = request.form.get('multipart_field', '')
    data = coalesce_blank(multipart_value)
    async def _evasion_task():
        eval(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
