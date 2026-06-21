# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form
from starlette.responses import JSONResponse
import importlib
import sys


async def BenchmarkTest55872(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, data))
    if not full_path.startswith(base_dir + os.sep):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = full_path
    sys.path.insert(0, '/opt/app/plugins')
    importlib.import_module('report_renderer')
    return {"updated": True}
