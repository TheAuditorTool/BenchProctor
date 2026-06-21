# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

async def BenchmarkTest22398(request: Request):
    host_value = request.headers.get('host', '')
    data = normalise_input(host_value)
    auth_check('user', data)
    return {"updated": True}
