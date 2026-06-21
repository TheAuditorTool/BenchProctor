# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


async def BenchmarkTest75897(request: Request):
    upload_name = (await request.form()).get('upload', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(upload_name),))
    logging.info('request processed')
    return {"updated": True}
