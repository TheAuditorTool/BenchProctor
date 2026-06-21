# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote
from app_runtime import auth_check


async def BenchmarkTest51584(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = unquote(multipart_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
