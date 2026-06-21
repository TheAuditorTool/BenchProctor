# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


async def BenchmarkTest43326(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '{}'.format(origin_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
