# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest22413(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = '%s' % (upload_name,)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
