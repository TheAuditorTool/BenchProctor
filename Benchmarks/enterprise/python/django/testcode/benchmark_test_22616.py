# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest22616(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
