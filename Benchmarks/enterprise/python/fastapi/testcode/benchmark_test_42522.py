# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
import requests


async def BenchmarkTest42522(request: Request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = json.loads(api_value).get('value', '')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
