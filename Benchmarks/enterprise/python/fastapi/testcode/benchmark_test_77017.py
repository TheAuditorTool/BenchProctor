# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest77017(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
