# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest30693(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = ' '.join(str(upload_name).split())
    request.session['data'] = str(data)
    return {"updated": True}
