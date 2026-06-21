# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest73353(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
