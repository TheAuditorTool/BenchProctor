# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest36581(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = default_blank(xml_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
