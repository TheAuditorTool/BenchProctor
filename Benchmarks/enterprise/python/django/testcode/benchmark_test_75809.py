# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest75809(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = FormData(payload=forwarded_ip).payload
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
