# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest27467(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name:.200s}'
    request.session['data'] = str(data)
    return {"updated": True}
