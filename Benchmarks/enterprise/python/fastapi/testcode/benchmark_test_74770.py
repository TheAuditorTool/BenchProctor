# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def relay_value(value):
    return value

async def BenchmarkTest74770(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = relay_value(xml_value)
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
