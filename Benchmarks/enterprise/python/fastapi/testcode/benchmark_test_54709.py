# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest54709(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
