# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import auth_check


async def BenchmarkTest24542(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    auth_check('user', data)
    return {"updated": True}
