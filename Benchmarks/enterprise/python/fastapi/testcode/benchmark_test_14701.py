# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest14701(request: Request):
    host_value = request.headers.get('host', '')
    data = '{}'.format(host_value)
    os.system('echo ' + str(data))
    return {"updated": True}
