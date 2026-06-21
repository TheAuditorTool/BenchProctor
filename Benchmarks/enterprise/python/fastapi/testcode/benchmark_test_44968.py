# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest44968(request: Request):
    upload_name = (await request.form()).get('upload', '')
    if upload_name:
        data = upload_name
    else:
        data = ''
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
