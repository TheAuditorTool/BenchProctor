# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest23694(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = (lambda v: v.strip())(upload_name)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
