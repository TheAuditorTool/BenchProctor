# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


async def BenchmarkTest75899(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = str(dotenv_value).replace('\x00', '')
    auth_check('user', data)
    return {"updated": True}
