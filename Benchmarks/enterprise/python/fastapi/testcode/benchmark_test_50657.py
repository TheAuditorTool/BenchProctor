# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest50657(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
