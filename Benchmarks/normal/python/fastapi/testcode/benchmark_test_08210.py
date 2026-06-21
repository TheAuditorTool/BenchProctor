# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import auth_check


async def BenchmarkTest08210(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % str(field_value)
    auth_check('user', data)
    return {"updated": True}
