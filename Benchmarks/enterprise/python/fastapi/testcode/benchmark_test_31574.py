# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest31574(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = '{}'.format(upload_name)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
