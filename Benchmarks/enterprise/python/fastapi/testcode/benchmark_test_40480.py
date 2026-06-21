# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest40480(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = ' '.join(str(upload_name).split())
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
