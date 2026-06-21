# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import json


async def BenchmarkTest05795(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    try:
        data = json.loads(yaml_value).get('value', yaml_value)
    except (json.JSONDecodeError, AttributeError):
        data = yaml_value
    logging.info('User action: ' + str(data))
    return {"updated": True}
