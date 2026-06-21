# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest60049(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    request.session['data'] = str(data)
    return {"updated": True}
