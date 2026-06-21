# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from app_runtime import auth_check


async def BenchmarkTest02474(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return {"updated": True}
