# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def normalise_input(value):
    return value.strip()

def BenchmarkTest41004():
    upload_name = request.files['upload'].filename
    data = normalise_input(upload_name)
    async def _evasion_task():
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
