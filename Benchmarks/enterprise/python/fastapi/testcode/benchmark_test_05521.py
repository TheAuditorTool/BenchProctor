# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05521(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    request.session['data'] = str(data)
    return {"updated": True}
