# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest44572(request: Request):
    upload_name = request.query_params.get('filename', '')
    data = '%s' % str(upload_name)
    os.unlink('/var/app/data/' + str(data))
    return {"updated": True}
