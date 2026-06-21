# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import importlib
import sys


def coalesce_blank(value):
    return value or ''

def BenchmarkTest07369():
    ua_value = request.headers.get('User-Agent', '')
    data = coalesce_blank(ua_value)
    async def _evasion_task():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
