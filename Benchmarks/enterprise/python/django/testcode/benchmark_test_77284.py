# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from dataclasses import dataclass
import sys


@dataclass
class FormData:
    payload: str

def BenchmarkTest77284(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = FormData(payload=argv_value).payload
    os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
