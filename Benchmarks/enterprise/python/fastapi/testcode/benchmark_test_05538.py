# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

async def BenchmarkTest05538(request: Request, field: str = Form('')):
    field_value = field
    data = normalise_input(field_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
