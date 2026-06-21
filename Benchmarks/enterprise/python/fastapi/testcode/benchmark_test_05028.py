# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05028(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = '{}'.format(upload_name)
    eval(str(data))
    return {"updated": True}
