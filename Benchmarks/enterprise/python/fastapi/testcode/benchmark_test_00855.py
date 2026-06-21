# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest00855(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name}'
    logging.info('User action: ' + str(data))
    return {"updated": True}
