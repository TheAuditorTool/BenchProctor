# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from urllib.parse import unquote


async def BenchmarkTest12724(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
