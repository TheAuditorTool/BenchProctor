# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import requests


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest55227(request: Request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = RequestPayload(api_value).value
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
