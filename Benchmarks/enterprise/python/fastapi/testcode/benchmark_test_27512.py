# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from fastapi import Form


async def BenchmarkTest27512(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    logging.info('User action: ' + str(data))
    return {"updated": True}
