# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest02141(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = '{}'.format(upload_name)
    request.session['user'] = str(data)
    return {"updated": True}
