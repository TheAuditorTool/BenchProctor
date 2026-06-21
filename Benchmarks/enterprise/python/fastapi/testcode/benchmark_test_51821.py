# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest51821(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
