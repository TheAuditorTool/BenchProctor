# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


async def BenchmarkTest02890(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(xml_value),))
    logging.info('request processed')
    return {"updated": True}
