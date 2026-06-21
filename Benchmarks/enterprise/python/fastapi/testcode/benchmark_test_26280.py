# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest26280(request: Request, field: str = Form('')):
    field_value = field
    reader = make_reader(field_value)
    data = reader()
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
