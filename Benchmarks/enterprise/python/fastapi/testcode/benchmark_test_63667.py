# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest63667(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
