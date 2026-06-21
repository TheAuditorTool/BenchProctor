# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import requests


async def BenchmarkTest79923(request: Request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = ' '.join(str(api_value).split())
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
