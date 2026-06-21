# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest68097(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    os.chmod('/var/app/data/' + str(xml_value), 0o777)
    return {"updated": True}
