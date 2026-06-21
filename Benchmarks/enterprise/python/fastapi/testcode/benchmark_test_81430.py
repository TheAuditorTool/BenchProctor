# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import defusedxml.ElementTree


async def BenchmarkTest81430(request: Request, field: str = Form('')):
    field_value = field
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(field_value)
    data = collected
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
