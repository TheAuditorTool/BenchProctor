# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from pydantic import BaseModel
from starlette.responses import JSONResponse
import importlib
import sys


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest31053(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = '/var/app/data/' + data
    sys.path.insert(0, '/opt/app/plugins')
    importlib.import_module('report_renderer')
    return {"updated": True}
