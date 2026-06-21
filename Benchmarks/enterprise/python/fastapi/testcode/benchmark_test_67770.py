# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest67770(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name:.200s}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
