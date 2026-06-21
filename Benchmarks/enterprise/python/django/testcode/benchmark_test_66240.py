# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest66240(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
