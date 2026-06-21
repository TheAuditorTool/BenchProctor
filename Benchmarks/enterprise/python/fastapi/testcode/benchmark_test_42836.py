# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest42836(request: Request):
    upload_name = request.query_params.get('filename', '')
    data = upload_name if upload_name else 'default'
    os.unlink('/var/app/data/' + str(data))
    return {"updated": True}
