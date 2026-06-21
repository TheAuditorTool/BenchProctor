# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest59966(request: Request):
    upload_name = (await request.form()).get('upload', '')
    auth_check('user', upload_name)
    return {"updated": True}
