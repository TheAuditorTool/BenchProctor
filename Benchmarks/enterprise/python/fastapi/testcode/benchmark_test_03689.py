# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest03689(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = default_blank(dotenv_value)
    auth_check('user', data)
    return {"updated": True}
