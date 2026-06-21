# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest23159():
    multipart_value = request.form.get('multipart_field', '')
    data = default_blank(multipart_value)
    async def _evasion_task():
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
