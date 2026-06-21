# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest58456(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
