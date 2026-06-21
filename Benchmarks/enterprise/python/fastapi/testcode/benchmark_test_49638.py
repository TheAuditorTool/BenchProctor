# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest49638(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    request.session['user'] = str(data)
    return {"updated": True}
