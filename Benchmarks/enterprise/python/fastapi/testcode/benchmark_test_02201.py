# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest02201(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = default_blank(raw_body)
    auth_check('user', data)
    return {"updated": True}
