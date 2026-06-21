# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def coalesce_blank(value):
    return value or ''

def BenchmarkTest37015():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = coalesce_blank(forwarded_ip)
    async def _evasion_task():
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
