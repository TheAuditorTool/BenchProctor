# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest07632(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    reader = make_reader(dotenv_value)
    data = reader()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
