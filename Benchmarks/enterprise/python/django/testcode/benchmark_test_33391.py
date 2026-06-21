# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest33391(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = FormData(payload=dotenv_value).payload
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
