# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import urllib.request
import urllib.parse
import ssl


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest77091(request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    ctx = ssl.create_default_context()
    ctx.set_ciphers('aNULL')
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
