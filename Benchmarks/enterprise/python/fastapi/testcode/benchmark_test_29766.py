# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


def normalise_input(value):
    return value.strip()

async def BenchmarkTest29766(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = normalise_input(forwarded_ip)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
