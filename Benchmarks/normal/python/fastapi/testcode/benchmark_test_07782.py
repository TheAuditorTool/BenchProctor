# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def normalise_input(value):
    return value.strip()

async def BenchmarkTest07782(request: Request):
    host_value = request.headers.get('host', '')
    data = normalise_input(host_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
