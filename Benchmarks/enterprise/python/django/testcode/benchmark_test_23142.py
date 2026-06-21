# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import json


def BenchmarkTest23142(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    def normalize(value):
        return value.strip()
    data = normalize(json_value)
    return HttpResponse(str(data), content_type='text/html')
