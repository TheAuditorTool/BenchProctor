# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest35726(request: Request):
    upload_name = (await request.form()).get('upload', '')
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    request.session['data'] = str(data)
    return {"updated": True}
