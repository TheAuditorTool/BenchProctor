# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

async def BenchmarkTest32076(request: Request):
    origin_value = request.headers.get('origin', '')
    data = normalise_input(origin_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
