# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


async def BenchmarkTest10127(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value}'
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
