# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


async def BenchmarkTest72797(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data, _sep, _rest = str(dotenv_value).partition('\x00')
    auth_check('user', data)
    return {"updated": True}
