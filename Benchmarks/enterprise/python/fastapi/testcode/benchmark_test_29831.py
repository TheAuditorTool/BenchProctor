# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest29831(request: Request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = default_blank(api_value)
    json.loads(data)
    return {"updated": True}
