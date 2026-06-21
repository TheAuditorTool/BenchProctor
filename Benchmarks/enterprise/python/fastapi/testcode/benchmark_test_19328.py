# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

async def BenchmarkTest19328(request: Request):
    origin_value = request.headers.get('origin', '')
    data = to_text(origin_value)
    auth_check('user', data)
    return {"updated": True}
