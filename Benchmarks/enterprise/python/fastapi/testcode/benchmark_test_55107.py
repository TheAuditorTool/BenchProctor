# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest55107(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    auth_check('user', multipart_value)
    return {"updated": True}
