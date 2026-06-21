# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest31976(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    int(str(data))
    return {"updated": True}
