# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest03831(request: Request, field: str = Form('')):
    field_value = field
    reader = make_reader(field_value)
    data = reader()
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
