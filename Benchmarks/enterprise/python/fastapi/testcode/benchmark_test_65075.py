# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest65075(request: Request):
    upload_name = (await request.form()).get('upload', '')
    logging.info('User action: ' + str(upload_name))
    return {"updated": True}
