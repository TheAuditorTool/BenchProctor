# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest33643(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = '%s' % str(file_value)
    auth_check('user', data)
    return {"updated": True}
