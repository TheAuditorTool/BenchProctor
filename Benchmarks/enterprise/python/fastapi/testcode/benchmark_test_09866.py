# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest09866(request: Request, field: str = Form('')):
    field_value = field
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(field_value))
    return {"updated": True}
