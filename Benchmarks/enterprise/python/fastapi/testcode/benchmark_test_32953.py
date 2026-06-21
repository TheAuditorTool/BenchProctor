# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


async def BenchmarkTest32953(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = f'{dotenv_value:.200s}'
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
