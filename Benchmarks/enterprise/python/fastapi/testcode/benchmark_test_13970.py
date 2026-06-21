# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

async def BenchmarkTest13970(request: Request):
    path_value = request.path_params.get('id', '')
    data = to_text(path_value)
    auth_check('user', data)
    return {"updated": True}
