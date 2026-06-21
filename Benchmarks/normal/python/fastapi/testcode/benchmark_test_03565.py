# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest03565(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
