# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import auth_check


async def BenchmarkTest77866(request: Request, field: str = Form('')):
    field_value = field
    auth_check('user', field_value)
    return {"updated": True}
