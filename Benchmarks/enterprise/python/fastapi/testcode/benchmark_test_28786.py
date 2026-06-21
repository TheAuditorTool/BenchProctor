# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest28786(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = str(upload_name).replace('\x00', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
