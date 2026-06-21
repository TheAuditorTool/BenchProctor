# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json
import requests


async def BenchmarkTest14293(request: Request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    prefix = ''
    data = prefix + str(api_value)
    yaml.safe_load(data)
    return {"updated": True}
