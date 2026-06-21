# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


async def BenchmarkTest02726(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % (referer_value,)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
