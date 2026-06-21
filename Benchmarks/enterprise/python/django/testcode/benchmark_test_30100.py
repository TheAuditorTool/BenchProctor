# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re


def relay_value(value):
    return value

def BenchmarkTest30100(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = relay_value(multipart_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    requests.get(str(data))
    return JsonResponse({"saved": True})
