# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


async def BenchmarkTest26550(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    auth_check('user', dotenv_value)
    return {"updated": True}
