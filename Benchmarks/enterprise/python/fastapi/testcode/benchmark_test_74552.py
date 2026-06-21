# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest74552(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    logging.info('User action: ' + str(xml_value))
    return {"updated": True}
