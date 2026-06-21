# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest80073(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % str(host_value)
    os.system('echo ' + str(data))
    return {"updated": True}
