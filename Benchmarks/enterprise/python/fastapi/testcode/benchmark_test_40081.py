# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import defusedxml.ElementTree


async def BenchmarkTest40081(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
