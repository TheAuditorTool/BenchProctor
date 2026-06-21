# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


async def BenchmarkTest29928(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(dotenv_value), store_cred)
    return {"updated": True}
