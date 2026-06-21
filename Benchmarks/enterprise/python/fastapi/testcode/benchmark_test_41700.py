# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from app_runtime import db


async def BenchmarkTest41700(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(comment_value).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
