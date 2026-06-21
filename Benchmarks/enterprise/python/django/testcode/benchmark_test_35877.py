# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest35877(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(dotenv_value))
    return JsonResponse({"saved": True})
