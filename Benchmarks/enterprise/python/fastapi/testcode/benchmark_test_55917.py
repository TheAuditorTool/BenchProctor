# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest55917(request: Request):
    upload_name = (await request.form()).get('upload', '')
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
