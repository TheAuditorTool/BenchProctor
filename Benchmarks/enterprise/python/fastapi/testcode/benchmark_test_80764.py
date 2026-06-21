# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest80764(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = upload_name if upload_name else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
