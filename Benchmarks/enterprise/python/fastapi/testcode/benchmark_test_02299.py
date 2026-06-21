# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from fastapi import Form


async def BenchmarkTest02299(request: Request, field: str = Form('')):
    field_value = field
    if field_value:
        data = field_value
    else:
        data = ''
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
