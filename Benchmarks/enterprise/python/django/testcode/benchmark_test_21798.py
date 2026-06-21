# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest21798(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
