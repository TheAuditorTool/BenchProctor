# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest02573(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
