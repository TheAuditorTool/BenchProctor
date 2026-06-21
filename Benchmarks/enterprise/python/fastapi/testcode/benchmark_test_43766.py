# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import json


async def BenchmarkTest43766(request: Request):
    upload_name = (await request.form()).get('upload', '')
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    logging.info('User action: ' + str(data))
    return {"updated": True}
