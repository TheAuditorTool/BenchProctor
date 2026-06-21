# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest75285(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    request.session['user'] = str(data)
    return {"updated": True}
