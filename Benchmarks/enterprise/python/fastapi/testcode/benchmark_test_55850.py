# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from fastapi import Form


async def BenchmarkTest55850(request: Request, field: str = Form('')):
    field_value = field
    data, _sep, _rest = str(field_value).partition('\x00')
    yaml.safe_load(data)
    return {"updated": True}
