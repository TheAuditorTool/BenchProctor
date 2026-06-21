# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


async def BenchmarkTest71218(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(multipart_value),))
    logging.info('request processed')
    return {"updated": True}
