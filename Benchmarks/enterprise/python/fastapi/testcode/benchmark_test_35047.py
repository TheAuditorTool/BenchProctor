# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
import os
from starlette.responses import JSONResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest35047(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
