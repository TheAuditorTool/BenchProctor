# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


async def BenchmarkTest46394(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
