# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest16860(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
