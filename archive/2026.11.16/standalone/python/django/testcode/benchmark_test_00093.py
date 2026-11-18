# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect
import requests


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00093(request):
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    data = RequestPayload(api_value).value
    return redirect(str(data))
