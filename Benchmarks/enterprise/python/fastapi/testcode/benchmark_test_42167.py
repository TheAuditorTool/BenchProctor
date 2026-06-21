# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest42167(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = (lambda v: v.strip())(xml_value)
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
