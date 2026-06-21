# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest30653(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data, _sep, _rest = str(upload_name).partition('\x00')
    request.session['user'] = str(data)
    return {"updated": True}
