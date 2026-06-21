# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest03273(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    logging.info('User action: ' + str(data))
    return {"updated": True}
