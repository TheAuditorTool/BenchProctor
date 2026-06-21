# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest33536(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    processed = shlex.quote(xml_value)
    os.system('echo ' + str(processed))
    return {"updated": True}
