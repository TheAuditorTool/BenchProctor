# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from fastapi import Form


async def BenchmarkTest33114(request: Request, field: str = Form('')):
    field_value = field
    data = '{}'.format(field_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
