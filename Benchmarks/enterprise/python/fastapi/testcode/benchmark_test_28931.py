# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


async def BenchmarkTest28931(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = '%s' % (dotenv_value,)
    auth_check('user', data)
    return {"updated": True}
