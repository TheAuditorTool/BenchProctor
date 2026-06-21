# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest66235(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value}'
    os.seteuid(65534)
    return {"updated": True}
