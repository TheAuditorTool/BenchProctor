# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest06043(request: Request):
    path_value = request.path_params.get('id', '')
    data = '%s' % str(path_value)
    auth_check('user', data)
    return {"updated": True}
