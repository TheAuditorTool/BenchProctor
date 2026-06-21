# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest45544(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    request.session['data'] = str(data)
    return {"updated": True}
