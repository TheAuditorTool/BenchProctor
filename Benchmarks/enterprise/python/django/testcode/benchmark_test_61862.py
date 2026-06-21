# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import sys


@dataclass
class FormData:
    payload: str

def BenchmarkTest61862(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = FormData(payload=argv_value).payload
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
