# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest56197(request: Request, field: str = Form('')):
    field_value = field
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
