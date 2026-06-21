# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


def normalise_input(value):
    return value.strip()

async def BenchmarkTest76530(request: Request, field: str = Form('')):
    field_value = field
    data = normalise_input(field_value)
    def _primary():
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
