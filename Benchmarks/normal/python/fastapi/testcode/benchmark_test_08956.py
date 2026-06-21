# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest08956(request: Request):
    upload_name = request.query_params.get('filename', '')
    os.unlink('/var/app/data/' + str(upload_name))
    return {"updated": True}
