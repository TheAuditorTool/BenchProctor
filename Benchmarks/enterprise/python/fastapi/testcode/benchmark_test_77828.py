# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest77828(request: Request):
    upload_name = (await request.form()).get('upload', '')
    if upload_name:
        data = upload_name
    else:
        data = ''
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
