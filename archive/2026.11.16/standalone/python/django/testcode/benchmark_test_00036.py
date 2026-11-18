# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00036(request):
    upload_name = request.FILES['doc'].name
    form = FormData(payload=upload_name)
    data = form.payload
    os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
