# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest60937(request: Request):
    upload_name = (await request.form()).get('upload', '')
    try:
        result = int(str(upload_name))
    except Exception:
        pass
    return {"updated": True}
