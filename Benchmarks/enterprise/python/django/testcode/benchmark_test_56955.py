# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest56955(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
