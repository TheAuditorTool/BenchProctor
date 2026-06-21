# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest58335(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    logging.info('User action: ' + str(data))
    return {"updated": True}
