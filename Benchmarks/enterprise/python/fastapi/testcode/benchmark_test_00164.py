# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest00164(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    logging.info('User action: ' + str(data))
    return {"updated": True}
