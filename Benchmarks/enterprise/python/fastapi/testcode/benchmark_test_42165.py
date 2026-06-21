# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest42165(request: Request):
    upload_name = (await request.form()).get('upload', '')
    prefix = ''
    data = prefix + str(upload_name)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
