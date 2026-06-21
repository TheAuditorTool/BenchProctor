# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest11927(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name}'
    auth_check('user', data)
    return {"updated": True}
