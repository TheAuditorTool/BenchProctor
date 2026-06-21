# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import auth_check


async def BenchmarkTest19847(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    auth_check('user', data)
    return {"updated": True}
