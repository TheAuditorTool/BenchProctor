# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from fastapi import Form
from app_runtime import auth_check


async def BenchmarkTest69566(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    auth_check('user', data)
    return {"updated": True}
