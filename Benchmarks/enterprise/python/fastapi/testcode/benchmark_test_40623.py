# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest40623(request: Request):
    upload_name = (await request.form()).get('upload', '')
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
