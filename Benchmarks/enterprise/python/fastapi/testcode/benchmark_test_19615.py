# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest19615(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = ' '.join(str(upload_name).split())
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
