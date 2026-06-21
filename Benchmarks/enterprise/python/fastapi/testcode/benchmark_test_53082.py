# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


async def BenchmarkTest53082(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = '%s' % str(multipart_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
