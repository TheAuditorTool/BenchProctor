# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


async def BenchmarkTest41226(request: Request):
    path_value = request.path_params.get('id', '')
    data = '%s' % (path_value,)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
