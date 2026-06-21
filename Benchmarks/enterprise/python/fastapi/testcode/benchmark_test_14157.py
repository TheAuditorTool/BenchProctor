# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest14157(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
