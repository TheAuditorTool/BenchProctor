# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest31142(request: Request):
    upload_name = (await request.form()).get('upload', '')
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    result = 100 / int(str(data))
    return {"updated": True}
