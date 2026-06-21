# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest20733(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    result = 100 / int(str(data))
    return {"updated": True}
