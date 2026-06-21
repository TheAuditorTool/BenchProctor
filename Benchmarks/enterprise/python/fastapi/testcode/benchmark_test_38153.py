# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import importlib
import sys


async def BenchmarkTest38153(request: Request):
    host_value = request.headers.get('host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = '/var/app/data/' + data
    sys.path.insert(0, '/opt/app/plugins')
    importlib.import_module('report_renderer')
    return {"updated": True}
