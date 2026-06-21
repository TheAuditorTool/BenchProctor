# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os


def BenchmarkTest19270(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    try:
        data = json.loads(dotenv_value).get('value', dotenv_value)
    except (json.JSONDecodeError, AttributeError):
        data = dotenv_value
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
