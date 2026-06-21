# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest00544(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = '%s' % str(upload_name)
    eval(str(data))
    return {"updated": True}
