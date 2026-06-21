# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import auth_check


async def BenchmarkTest65306(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    auth_check('user', data)
    return {"updated": True}
