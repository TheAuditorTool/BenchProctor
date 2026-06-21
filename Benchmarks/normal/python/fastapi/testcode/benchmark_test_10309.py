# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


async def BenchmarkTest10309(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % str(referer_value)
    yaml.safe_load(data)
    return {"updated": True}
