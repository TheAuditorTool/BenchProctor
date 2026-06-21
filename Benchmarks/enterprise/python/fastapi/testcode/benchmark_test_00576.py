# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest00576(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    kind = 'json' if str(yaml_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = yaml_value
            data = parsed
        case _:
            data = yaml_value
    auth_check('user', data)
    return {"updated": True}
