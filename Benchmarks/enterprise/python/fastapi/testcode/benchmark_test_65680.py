# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def relay_value(value):
    return value

async def BenchmarkTest65680(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = relay_value(multipart_value)
    async def _evasion_task():
        eval(str(data))
    await _evasion_task()
    return {"updated": True}
