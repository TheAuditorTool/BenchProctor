# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest00833(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = upload_name if upload_name else 'default'
    request.session['user'] = str(data)
    return {"updated": True}
