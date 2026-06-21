# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest46814(request: Request, field: str = Form('')):
    field_value = field
    data = ' '.join(str(field_value).split())
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
