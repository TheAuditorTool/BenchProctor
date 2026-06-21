# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest73649(request: Request):
    upload_name = (await request.form()).get('upload', '')
    globals().setdefault('_secret_cache', {})['current'] = str(upload_name)
    return {"updated": True}
