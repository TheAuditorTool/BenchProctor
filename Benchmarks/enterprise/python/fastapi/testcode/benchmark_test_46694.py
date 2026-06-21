# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest46694(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    int(str(multipart_value))
    return {"updated": True}
