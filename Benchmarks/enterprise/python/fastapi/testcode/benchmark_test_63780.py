# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest63780(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = str(upload_name).replace('\x00', '')
    request.session['user'] = str(data)
    return {"updated": True}
