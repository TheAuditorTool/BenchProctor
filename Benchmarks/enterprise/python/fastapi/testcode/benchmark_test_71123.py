# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest71123(request: Request, field: str = Form('')):
    field_value = field
    data = default_blank(field_value)
    auth_check('user', data)
    return {"updated": True}
