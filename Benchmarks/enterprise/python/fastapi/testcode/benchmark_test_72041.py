# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest72041(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = default_blank(config_value)
    auth_check('user', data)
    return {"updated": True}
