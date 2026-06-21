# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest77852(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    result = 100 / int(str(data))
    return {"updated": True}
