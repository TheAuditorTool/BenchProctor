# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from fastapi import Form
import json


async def BenchmarkTest32074(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    logging.info('User action: ' + str(data))
    return {"updated": True}
