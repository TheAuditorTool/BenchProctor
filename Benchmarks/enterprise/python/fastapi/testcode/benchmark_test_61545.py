# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest61545(request: Request):
    path_value = request.path_params.get('id', '')
    reader = make_reader(path_value)
    data = reader()
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return JSONResponse({'config_set': 'APP_USER_PREFERENCE'}, status_code=200)
