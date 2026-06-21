# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest78772(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = f'{multipart_value}'
    exec(str(data))
    return {"updated": True}
