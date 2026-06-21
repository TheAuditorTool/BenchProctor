# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest02705(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = (lambda v: v.strip())(upload_name)
    auth_check('user', data)
    return {"updated": True}
