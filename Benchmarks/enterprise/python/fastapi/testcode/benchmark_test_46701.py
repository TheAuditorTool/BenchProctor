# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import defusedxml.ElementTree


async def BenchmarkTest46701(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % str(field_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
